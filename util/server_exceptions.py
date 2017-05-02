# -*- coding: utf-8 -*-
import json

class ServerCommonException(Exception):
    def __init__(self, code=0, debug_message='', output_message=''):
        self.code = code
        self.output_message = output_message
        self.debug_message = debug_message

    def debug_info(self):
        return json.dumps({'output_msg': self.output_message, 'debug_msg': self.debug_message})

    def __str__(self):
        return self.debug_info()

    __unicode__ = __str__


class NormalError(ServerCommonException):
    def __init__(self, code=0, debug_message='', output_message='', data=None):
        self.data = data
        super(NormalError, self).__init__(code, debug_message, output_message)

    def debug_info(self):
        return '%s,%s' % (self.output_message, self.debug_message)


class WrongParameterError(ServerCommonException):
    def __init__(self, code=0, debug_message='', output_message=''):
        super(WrongParameterError, self).__init__(code, debug_message, output_message)


class CallbackReturnError(ServerCommonException):
    def __init__(self, code=0, debug_message='', output_message=''):
        super(CallbackReturnError, self).__init__(code, debug_message, output_message)


class ThirdAPIResponseError(ServerCommonException):
    DATA_SOURCE_NETWORK_ERROR = 100
    DATA_SOURCE_REQUEST_TIMEOUT = 101
    code_output_message_mapping = {
        DATA_SOURCE_NETWORK_ERROR: u'网络繁忙，稍后重试',
        DATA_SOURCE_REQUEST_TIMEOUT: u'网络繁忙，稍后重试'
    }

    def __init__(self, code=0, debug_message='', output_message='', method='', url='', req_header='', req_str='', resp_body='', resp_header='', error=''):
        self.code = code
        self.output_message = output_message or self.code_output_message_mapping.get(code, '')
        self.debug_message = debug_message or {'method': method, 'url': url, 'req_header': req_header, 'req_str': req_str, 'resp_body': resp_body, 'resp_header': resp_header, 'error': error}
