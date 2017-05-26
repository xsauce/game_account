# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

import settings
import util.base_handler
from game_account.logic import GameInfo, CloseBill
from game_account.model import GameCloseBillHistoryModel
from login.model import SessionModel
from util.pt_tornado_logging import PTTornadoLogger


class GameAccountStaticFileHandler(util.base_handler.BaseStaticFileHandler):
    ROUTE = r'/static/game_account/(.*)'
    ROUTE_PARAM = dict(path=os.path.join(settings.ROOT_DIR, 'game_account', 'static'))

class GameAccountHandler(util.base_handler.BaseHandler):
    ROUTE = r'/game_account/(.*)'
    TEMPLATE_DIR = os.path.join(settings.ROOT_DIR, 'game_account', 'template')
    def __init__(self, *args, **kwargs):
        super(GameAccountHandler, self).__init__(*args, **kwargs)

    def prepare(self):
        super(GameAccountHandler, self).prepare()
        token = self.get_secure_cookie('token', None)
        PTTornadoLogger().info('token:%s' % token)
        if token is None:
            self.redirect('/login/index')
        else:
            expired_point = SessionModel().select_field(['expired_point']).where({'session_key': token}).get_one(dict_result_bool=False)[0]
            if expired_point <= datetime.now():
                self.redirect('/login/index')

    def index_action(self):
        self.output_template('index.html')

    def game_list_action(self):
        self.output_template('game_list.html')

    def games_action(self):
        self.output_json(data=GameInfo().get_all())

    def add_game_action(self):
        json_body = json.loads(self.request.body)
        GameInfo().create_one(json_body['game_id'], json_body['score_to_money_rate'], json_body['result'])
        self.output_json()

    def edit_game_action(self):
        json_body = json.loads(self.request.body)
        GameInfo().update_one(json_body['game_pkid'], json_body['game_id'], json_body['score_to_money_rate'], json_body['game_finish_datetime'], json_body['result'])
        self.output_json()

    def del_game_action(self):
        game_pkid = self.get_argument_int('game_pkid')
        GameInfo().delete_one(game_pkid)
        self.output_json()

    def close_bill_action(self):
        fee_rate = self.get_argument_float('fee_rate')
        close_bill_check_point = self.get_argument('close_bill_check_point')

        try:
            close_bill_check_point = datetime.strptime(close_bill_check_point, '%Y-%m-%d %H:%M')
        except ValueError:
            close_bill_check_point = datetime.strptime(close_bill_check_point, '%Y-%m-%d %H:%M:%S')

        CloseBill().create_one(close_bill_check_point=close_bill_check_point, fee_rate=fee_rate)
        self.output_json()

    def close_bill_history_action(self):
        self.output_template('close_bill_history.html')

    def close_bill_histories_action(self):
        self.output_json(data=CloseBill().get_all())

    def del_close_bill_history_action(self):
        close_bill_history_pkid = self.get_argument_int('close_bill_history_pkid')
        CloseBill().delete_one(close_bill_history_pkid)
        self.output_json()

    def download_close_bill_history_detail_action(self):
        close_bill_history_pkid = self.get_argument_int('close_bill_history_pkid')
        history_row = GameCloseBillHistoryModel().where({'pkid': close_bill_history_pkid}).get_one()
        file = CloseBill().download_history_detail(close_bill_history_pkid)
        self.output_csv(history_row['close_bill_check_point'].replace(' ', 'T'), file)






