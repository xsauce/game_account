# -*- coding: utf-8 -*-
import json
import os

import sys
import tornado
import tornado.log
from logging import Logger

def currentframe():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        return sys.exc_info()[2].tb_frame.f_back

_srcfile = os.path.normcase(currentframe.__code__.co_filename)

TYPE_C2P = 'c2p'
TYPE_P2T = 'p2t'
TYPE_NORMAL = 'logic'

class PTTornadoLogger:
    def __init__(self, logger=None, url='', status_code='', method='', req_body='', resp_body='', cost_time='', log_type=TYPE_NORMAL):
        self._logger = logger or tornado.log.access_log
        self.url = url
        self.status_code = status_code
        self.method = method
        self.req_body = req_body if isinstance(req_body, str) else resp_body.encode('utf-8')
        self.resp_body = resp_body if isinstance(resp_body, str) else resp_body.encode('utf-8')
        self.cost_time = cost_time
        self.log_type = log_type

    def find_caller(self):
        """
        Find the stack frame of the caller so that we can note the source
        file name, line number and function name.
        """
        f = currentframe()
        #On some versions of IronPython, currentframe() returns None if
        #IronPython isn't run with -X:Frames.
        if f is not None:
            f = f.f_back
        rv = "(unknown file)", 0, "(unknown function)"
        while hasattr(f, "f_code"):
            co = f.f_code
            filename = os.path.normcase(co.co_filename)
            if filename == _srcfile:
                f = f.f_back
                continue
            rv = (co.co_filename, f.f_lineno, co.co_name)
            break
        return rv

    def create_request_str(self):
        fn, lno, func = self.find_caller()
        module = fn.rsplit('/', 1)[-1][:-3]
        return '{module}\t{func}\t{line_no}\t{uri}\t{status_code}\t{method}\t{req_body}\t{resp_body}\t{cost_time}\t{log_type}'.format(**{
                'module': module,
                'line_no': lno,
                'func': func,
                'uri': self.url,
                'method': self.method,
                'req_body': self.req_body,
                'resp_body': self.resp_body,
                'status_code': self.status_code,
                'cost_time': self.cost_time,
                'log_type': self.log_type
            })

    def info(self, msg, *args, **kwargs):
        self._logger.info(self.create_request_str() + '\t' + msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self._logger.debug(self.create_request_str() + '\t' + msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._logger.error(self.create_request_str() + '\t' + msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self._logger.warning(self.create_request_str() + '\t' + msg, *args, **kwargs)

    warn = warning

    def exception(self, msg, *args, **kwargs):
        self._logger.exception(self.create_request_str() + '\t' + msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self._logger.critical(self.create_request_str() + '\t' + msg, *args, **kwargs)

    fatal = critical

