# -*- coding: utf-8 -*-
import argparse
import logging
import logging.handlers
import sys
import traceback

import game_account.handler
from util import base_handler

sys.path.append('/usr/local/game_account/')
from util.base_handler import WorkingRequestCounter
import os
import functools
import signal
import time
import tornado.web
import tornado.ioloop
import tornado.log
import tornado.httpclient
from tornado.web import url
import settings
from settings import TORNADO_LOG_SETTINGS
import json
import tornado.httpserver
# import tornado.curl_httpclient.CurlAsyncHTTPClient

IS_STOPPING = False

def get_url_routes():
    handler_kw = 'Handler'
    ur = []
    handlers = [
        game_account.handler,
        base_handler
    ]
    for handler in handlers:
        for i in dir(handler):
            if i.endswith(handler_kw) and not i.startswith('Base'):
                handler_cls = getattr(handler, i)
                ur.append(url(handler_cls.ROUTE, handler_cls, handler_cls.ROUTE_PARAM, name=i[:-1 * len(handler_kw)]))
    return ur


def configuration_logging(**kwargs):
    log_dir = TORNADO_LOG_SETTINGS['log_file_prefix']
    TORNADO_LOG_SETTINGS.update(**kwargs)
    port = settings.TORNADO_SERVER_SETTINGS['port']
    for log_name, logger in [('tornado_access_%s.log' % port, tornado.log.access_log), ('tornado_app_%s.log' % port, tornado.log.app_log), ('tornado_gen_%s.log' % port, tornado.log.gen_log)]:
        log_file = os.path.join(log_dir, log_name)
        logger.setLevel(getattr(logging, TORNADO_LOG_SETTINGS['logging'].upper()))
        if log_file:
            rotate_mode = TORNADO_LOG_SETTINGS['log_rotate_mode']
            if rotate_mode == 'size':
                channel = logging.handlers.RotatingFileHandler(
                    filename=log_file,
                    maxBytes=TORNADO_LOG_SETTINGS['log_file_max_size'],
                    backupCount=TORNADO_LOG_SETTINGS['log_file_num_backups']
                )
            elif rotate_mode == 'time':
                channel = logging.handlers.TimedRotatingFileHandler(
                    filename=log_file,
                    when=TORNADO_LOG_SETTINGS['log_rotate_when'],
                    interval=TORNADO_LOG_SETTINGS['log_rotate_interval'],
                    backupCount=TORNADO_LOG_SETTINGS['log_file_num_backups'])
            else:
                error_message = 'The value of log_rotate_mode option should be ' + \
                                '"size" or "time", not "%s".' % rotate_mode
                raise ValueError(error_message)
            channel.setFormatter(tornado.log.LogFormatter(fmt=TORNADO_LOG_SETTINGS['log_fmt'], datefmt=TORNADO_LOG_SETTINGS['log_datefmt'], color=False))
            logger.addHandler(channel)

        if (TORNADO_LOG_SETTINGS['log_to_stderr'] or (TORNADO_LOG_SETTINGS['log_to_stderr'] is None and not logger.handlers)):
            # Set up color if we are in a tty and curses is installed
            channel = logging.StreamHandler()
            channel.setFormatter(tornado.log.LogFormatter(fmt=TORNADO_LOG_SETTINGS['log_fmt'], datefmt=TORNADO_LOG_SETTINGS['log_datefmt']))
            logger.addHandler(channel)


def pt_log_function(handler):
    pass

def sig_handler(server, sig, frame):
    tornado.log.app_log.info('catch_signal %s', sig)
    global IS_STOPPING
    if not IS_STOPPING:
        IS_STOPPING = True
        tornado.ioloop.IOLoop.current().add_callback_from_signal(functools.partial(shutdown, server))

def shutdown(server):
    tornado.log.app_log.info('start to shutdown server')
    server.stop()
    tornado.log.app_log.info('server do not accept new request')
    tornado.log.app_log.info('will shutdown in %s seconds', settings.TORNADO_SERVER_SETTINGS['wait_seconds_before_shutdown'])
    io_loop = tornado.ioloop.IOLoop.current()
    deadline = time.time() + settings.TORNADO_SERVER_SETTINGS['wait_seconds_before_shutdown']

    def stop_loop():
        now = io_loop.time()
        working_request_count = WorkingRequestCounter().get_working_request_count()
        if working_request_count > 0 and now < deadline:
            tornado.log.app_log.info('%d working requests' % working_request_count)
            io_loop.add_timeout(now + 1, stop_loop)
        else:
            io_loop.stop()
    stop_loop()


def start_server(port=None):
    try:
        settings.TORNADO_SERVER_SETTINGS['port'] = port
        configuration_logging()
        for i in dir(settings):
            if isinstance(getattr(settings, i), dict):
                if not i.startswith('_'):
                    tornado.log.app_log.debug('%s:%s' % (i, json.dumps(getattr(settings, i))))

        tornado_application_settings = settings.TORNADO_APPLICATION_SETTINGS
        tornado_application_settings['log_function'] = pt_log_function

        app = tornado.web.Application(get_url_routes(), **tornado_application_settings)
        server = tornado.httpserver.HTTPServer(app)
        partial_sig_handler = functools.partial(sig_handler, server)
        signal.signal(signal.SIGTERM, partial_sig_handler)
        signal.signal(signal.SIGINT, partial_sig_handler)
        if settings.TORNADO_SERVER_SETTINGS['multi_mode']:
            server.bind(settings.TORNADO_SERVER_SETTINGS['port'])
            server.start(settings.TORNADO_SERVER_SETTINGS['subprocess_num'])
        else:
            app.listen(settings.TORNADO_SERVER_SETTINGS['port'], address=settings.TORNADO_SERVER_SETTINGS['ip'])
        # tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient",
        #                                              max_clients=settings.TORNADO_SERVER_SETTINGS[
        #                                                  'async_max_http_client'])
        tornado.log.app_log.info('start server,listen %s:%s' % (settings.TORNADO_SERVER_SETTINGS['ip'], port))
        tornado.ioloop.IOLoop.current().start()
        tornado.log.app_log.info('finish to shutdown server')
    except SystemExit as e:
        if str(e) == '0':
            tornado.log.app_log.info('parent process exited normally')
        else:
            tornado.log.app_log.error('parent process exited by SystemExit(%s)' % e)
    except:
        tornado.log.app_log.error('terminate server %s, %s', json.dumps(traceback.format_exception(*sys.exc_info())))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', help='port num', default='9090')
    args = parser.parse_args()
    start_server(args.port)
