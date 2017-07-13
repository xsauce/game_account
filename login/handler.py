# -*- coding: utf-8 -*-
import json
import os
import uuid
from datetime import datetime, timedelta

import settings
from login.const_var import LoginCode
from login.model import UserModel, SessionModel, UserPrivModel
from util.base_handler import BaseHandler
from util.tool_func import md5


class LoginHandler(BaseHandler):
    ROUTE = '/login/(.*)'
    LOGIN_SUCCESS_REDIRECT_URL = '/game_account/overview'

    def get_template_path(self):
        return os.path.join(settings.ROOT_DIR, 'login', 'template')

    def index_action(self):
        err = self.get_argument('err', '')
        self.output_template('login.html', err=err)

    def login_action(self):
        username = self.get_argument('username')
        password = self.get_argument('password')

        user_rows = UserModel().select_field(['expired_at', 'pkid']).where({'username': username, 'password': md5(password)}).get_one()
        if user_rows:
            if user_rows['expired_at'] <= datetime.now():
                self.output_template('login.html', err=LoginCode.LOGIN_EXPIRED)
            else:
                token = uuid.uuid1().get_hex()
                SessionModel().insert_one_row({'session_key': token, 'expired_point': (datetime.now() + timedelta(days=30))})
                self.set_secure_cookie('token', token)
                self.set_secure_cookie('user_pkid', str(user_rows['pkid']))
                self.redirect(self.LOGIN_SUCCESS_REDIRECT_URL)
        else:
            self.output_template('login.html', err=LoginCode.LOGIN_ERROR)
