# -*- coding: utf-8 -*-
class CodeMappingMsg(object):
    def __init__(self, code, msg):
        self.code_msg_tuple = (code, msg)

    def __int__(self):
        return self.code_msg_tuple[0]

    def __str__(self):
        return self.code_msg_tuple[1]

class LoginCode:
    NO_LOGIN = CodeMappingMsg(100, u'您未登录,请先登录')
    LOGIN_EXPIRED = CodeMappingMsg(101, u'您登录有效期已过,请重新登录')
    LOGIN_ERROR = CodeMappingMsg(102, u'用户名密码错误')
    ACCOUNT_EXPIRED = CodeMappingMsg(200, u'账户使用过期')
    NO_PRIV = CodeMappingMsg(201, u'账号无权限')
