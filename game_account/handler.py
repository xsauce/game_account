# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

import settings
import util.base_handler
from game_account.logic import GameInfo, CloseBill
from game_account.model import GameCloseBillHistoryModel, GameTypeModel
from login.const_var import LoginCode
from login.model import SessionModel, UserPrivModel
from util.pt_tornado_logging import PTTornadoLogger


# class GameAccountStaticFileHandler(util.base_handler.BaseStaticFileHandler):
#     ROUTE = r'/static/game_account/(.*)'
#     ROUTE_PARAM = dict(path=os.path.join(settings.ROOT_DIR, 'game_account', 'static'))

class GameAccountHandler(util.base_handler.BaseHandler):
    ROUTE = r'/game_account/(.*)'
    TEMPLATE_DIR = os.path.join(settings.ROOT_DIR, 'game_account', 'template')
    def __init__(self, *args, **kwargs):
        super(GameAccountHandler, self).__init__(*args, **kwargs)
        self.is_ajax_request = False
        self.user_pkid = 0
        self.privs_list = []
        self.game_type_pkid = 0

    def redirect_relogin(self, err):
        redirect_url = '/login/index?err=%s' % err
        if self.is_ajax_request:
            self.output_json(code=util.base_handler.RspCode.REDIRECT, data={'redirect_url': redirect_url})
            self.finish()
        else:
            self.redirect(redirect_url)

    def prepare(self):
        super(GameAccountHandler, self).prepare()
        token = self.get_secure_cookie('token', None)
        PTTornadoLogger().info('token:%s' % token)
        self.is_ajax_request = self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        session_row = SessionModel().select_field(['expired_point']).where({'session_key': token}).get_one()
        if session_row is None or token is None:
            self.redirect_relogin(LoginCode.NO_LOGIN)
        elif session_row['expired_point'] <= datetime.now():
                self.redirect_relogin(LoginCode.LOGIN_EXPIRED)
        else:
            self.user_pkid = self.get_secure_cookie('user_pkid', None)
            if self.is_ajax_request:
                self.check_priv_by_game_type_pkid()

    def check_priv_by_game_type_pkid(self):
        privs_list = UserPrivModel().get_game_type_user_priv_list(self.user_pkid, self.get_argument('game_type_pkid'))
        if len(privs_list) == 0:
            self.redirect_relogin(LoginCode.NO_PRIV)
        else:
            self.privs_list = privs_list
            self.game_type_pkid = self.get_argument('game_type_pkid')

    def get_template_path(self):
        return os.path.join(settings.ROOT_DIR, 'game_account', 'template')

    def output_game_template(self, template_name, **kwargs):
        game_type_list = GameTypeModel().get_game_type_with_priv(self.user_pkid)
        game_type_pkid = self.get_argument('game_type_pkid', '0')
        kwargs.update({'game_type_pkid': game_type_pkid, 'game_type_list': game_type_list})
        self.output_template(template_name, **kwargs)

    def overview_action(self):
        self.output_game_template('overview.html')

    def game_list_action(self):
        self.check_priv_by_game_type_pkid()
        game_type_info = GameInfo().get_game_type_by_pkid(self.game_type_pkid)
        self.output_game_template('game_list.html', most_player_count=game_type_info['most_player_count'])

    def game_type_by_pkid_action(self):
        result = GameInfo().get_game_type_by_pkid(self.game_type_pkid)
        self.output_json(data=result)

    def games_action(self):
        self.output_json(data=GameInfo().get_all(self.game_type_pkid, self.user_pkid))

    def games_by_created_at_action(self):
        start_dt = self.get_argument_datetime('start_dt')
        end_dt = self.get_argument_datetime('end_dt')
        self.output_json(data=GameInfo().get_data_by_date(self.game_type_pkid, self.user_pkid, start_dt, end_dt))

    def add_game_action(self):
        json_body = json.loads(self.request.body)
        GameInfo().create_one(self.game_type_pkid, self.user_pkid, json_body['game_id'], json_body['score_to_money_rate'], json_body['result'])
        self.output_json()

    def edit_game_action(self):
        json_body = json.loads(self.request.body)
        GameInfo().update_one(self.game_type_pkid, self.user_pkid, json_body['game_pkid'], json_body['game_id'], json_body['score_to_money_rate'], json_body['game_finish_datetime'], json_body['result'])
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

        CloseBill().create_one(game_type_pkid=self.game_type_pkid, user_pkid=self.user_pkid, close_bill_check_point=close_bill_check_point, fee_rate=fee_rate)
        self.output_json()

    def close_bill_history_action(self):
        self.check_priv_by_game_type_pkid()
        self.output_game_template('close_bill_history.html')

    def close_bill_histories_action(self):
        self.output_json(data=CloseBill().get_all(game_type_pkid=self.game_type_pkid, user_pkid=self.user_pkid))

    def close_bill_histories_by_created_at_action(self):
        start_dt = self.get_argument_datetime('start_dt')
        end_dt = self.get_argument_datetime('end_dt')
        self.output_json(data=CloseBill().get_by_created_at(game_type_pkid=self.game_type_pkid, user_pkid=self.user_pkid, start_dt=start_dt, end_dt=end_dt))

    def del_close_bill_history_action(self):
        close_bill_history_pkid = self.get_argument_int('close_bill_history_pkid')
        CloseBill().delete_one(close_bill_history_pkid)
        self.output_json()

    def download_close_bill_history_detail_action(self):
        self.check_priv_by_game_type_pkid()
        close_bill_history_pkid = self.get_argument_int('close_bill_history_pkid')
        history_row = GameCloseBillHistoryModel().where({'pkid': close_bill_history_pkid}).get_one()
        file = CloseBill().download_history_detail(self.game_type_pkid, self.user_pkid, close_bill_history_pkid)
        self.output_csv(history_row['close_bill_check_point'].replace(' ', 'T'), file)

    def close_bill_history_player_detail_action(self):
        player_id = self.get_argument('player_id')
        close_bill_history_pkid = self.get_argument_int('close_bill_history_pkid')
        data = CloseBill().get_close_bill_history_player_detail(self.game_type_pkid, self.user_pkid, player_id, close_bill_history_pkid)
        self.output_json(data=data)







