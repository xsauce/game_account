# -*- coding: utf-8 -*-
import os
import uuid
from datetime import datetime, timedelta

import settings
from login.model import UserModel, SessionModel
from util.base_handler import BaseHandler
from util.tool_func import md5


class LoginHandler(BaseHandler):
    ROUTE = '/login/(.*)'
    TEMPLATE_DIR = os.path.join(settings.ROOT_DIR, 'login', 'template')

    def index_action(self):
        self.output_template('login.html', err='')

    def login_action(self):
        username = self.get_argument('username')
        password = self.get_argument('password')

        is_exist = UserModel().select_field(['count(1)']).where({'username': username, 'password': md5(password)}).get_one(dict_result_bool=False)
        if is_exist[0] > 0:
            token = uuid.uuid1().get_hex()
            SessionModel().insert_one_row({'session_key': token, 'expired_point': (datetime.now() + timedelta(days=7))})
            self.set_secure_cookie('token', token)
            self.redirect('/game_account/index')
        else:
            self.output_template('login.html', err=u'登录错误')
