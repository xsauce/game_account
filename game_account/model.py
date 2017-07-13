# -*- coding: utf-8 -*-
import util.base_model
from login.model import UserPrivModel


class GameInfoModel(util.base_model.BaseModel):
    _TABLE = 'game_info'
    def __init__(self):
        super(GameInfoModel, self).__init__()

    def get_all_with_result(self, game_type_pkid, user_pkid):
        sql = 'SELECT g.pkid, g.game_id, g.game_finish_datetime, g.score_to_money_rate, g.game_status, p.player_id, p.player_score FROM {0} g INNER JOIN {1} p on p.game_pkid=g.pkid WHERE g.game_type_pkid=%s and g.user_pkid=%s ORDER BY g.created_at DESC'.format(
            self._TABLE, GameResultModel._TABLE
        )
        return self.query_many_row(sql, (game_type_pkid, user_pkid))

    def get_data_by_date_with_result(self, game_type_pkid, user_pkid, start_dt, end_dt):
        sql = 'SELECT g.pkid, g.game_id, g.game_finish_datetime, g.score_to_money_rate, g.game_status, p.player_id, p.player_score FROM {0} g INNER JOIN {1} p on p.game_pkid=g.pkid WHERE g.created_at >=%s and g.created_at <=%s and g.game_type_pkid=%s and g.user_pkid=%s ORDER BY g.created_at DESC'.format(
            self._TABLE, GameResultModel._TABLE
        )
        return self.query_many_row(sql, (start_dt, end_dt, game_type_pkid, user_pkid))

    def delete_one(self, pkid):
        sql = 'DELETE FROM {0} WHERE pkid=%s'.format(self._TABLE)
        self.execute(sql, (pkid,))


class GameResultModel(util.base_model.BaseModel):
    _TABLE = 'game_result'
    def __init__(self):
        super(GameResultModel, self).__init__()

    def delete_by_game_pkid(self, game_pkid):
        sql = 'DELETE FROM {0} where game_pkid=%s'.format(self._TABLE)
        self.execute(sql, (game_pkid,))

class GameCloseBillHistoryModel(util.base_model.BaseModel):
    _TABLE = 'game_close_bill_history'
    def __init__(self):
        super(GameCloseBillHistoryModel, self).__init__()

    def get_all_with_detail(self, game_type_pkid, user_pkid):
        sql = 'SELECT close_bill_check_point, fee_rate, total_final_money, total_money, total_fee,total_game_count,player_id,final_money,money,game_count,fee,history_pkid FROM {0} h INNER JOIN {1} d on h.pkid=d.history_pkid WHERE h.game_type_pkid=%s and h.user_pkid=%s ORDER BY h.close_bill_check_point DESC'.format(
            self._TABLE, GameCloseBillHistoryDetailModel._TABLE
        )
        return self.query_many_row(sql, (game_type_pkid, user_pkid))

    def delete_one(self, pkid):
        sql = 'DELETE FROM {0} WHERE pkid=%s'.format(self._TABLE)
        self.execute(sql, (pkid,))

    def get_by_created_at_with_detail(self, game_type_pkid, user_pkid, start_dt, end_dt):
        sql = 'SELECT close_bill_check_point, fee_rate, total_final_money, total_money, total_fee,total_game_count,player_id,final_money,money,game_count,fee,history_pkid FROM {0} h INNER JOIN {1} d on h.pkid=d.history_pkid WHERE h.created_at >=%s and h.created_at <=%s and h.game_type_pkid=%s and h.user_pkid=%s ORDER BY h.close_bill_check_point DESC'.format(
            self._TABLE, GameCloseBillHistoryDetailModel._TABLE
        )
        return self.query_many_row(sql, (start_dt, end_dt, game_type_pkid, user_pkid))

class GameCloseBillHistoryDetailModel(util.base_model.BaseModel):
    _TABLE = 'game_close_bill_history_detail'

    def __init__(self):
        super(GameCloseBillHistoryDetailModel, self).__init__()

    def delete_by_history_id(self, history_id):
        sql = 'DELETE FROM {0} WHERE history_pkid=%s'.format(self._TABLE)
        self.execute(sql, (history_id,))

class GamePlayerModel(util.base_model.BaseModel):
    _TABLE = 'game_player'
    def __init__(self):
        super(GamePlayerModel, self).__init__()

class GameCloseBillGameModel(util.base_model.BaseModel):
    _TABLE = 'game_close_bill_history_game'
    def __init__(self):
        super(GameCloseBillGameModel, self).__init__()

    def delete_by_game_pkid(self, game_pkid):
        sql = 'DELETE FROM {0} WHERE game_pkid=%s'.format(self._TABLE)
        self.execute(sql, (game_pkid,))

    def delete_by_history_pkid(self, history_pkid):
        sql = 'DELETE FROM {0} WHERE history_pkid=%s'.format(self._TABLE)
        self.execute(sql, (history_pkid,))

    def set_status_game_id_by_close_history_pkid(self, history_pkid, status):
        sql = 'UPDATE {0} SET game_status=%s WHERE pkid in (SELECT game_pkid FROM {1} WHERE history_pkid=%s)'.format(
            GameInfoModel._TABLE,
            self._TABLE
        )
        self.execute(sql, (status, history_pkid))

class GameTypeModel(util.base_model.BaseModel):
    _TABLE = 'game_type'
    def __init__(self):
        super(GameTypeModel, self).__init__()

    def get_game_type_with_priv(self, user_pkid):
        sql = "SELECT g.type_desc, g.type_name, g.pkid FROM {0} g INNER JOIN {1} u on u.game_type_pkid=g.pkid WHERE user_pkid=%s".format(
            self._TABLE,
            UserPrivModel._TABLE
        )
        rows = self.query_many_row(sql, (user_pkid,))
        return rows