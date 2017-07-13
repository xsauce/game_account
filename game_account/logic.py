# -*- coding: utf-8 -*-
import StringIO
import csv
from collections import defaultdict, Counter

from game_account.model import GameInfoModel, GameResultModel, GameCloseBillHistoryModel, \
    GameCloseBillHistoryDetailModel, GameCloseBillGameModel, GameTypeModel
from util.server_exceptions import NormalError
from util.sql_helper import transaction_context


class GameInfo(object):
    def __init__(self):
        pass

    def list_by_pagination(self, page_index=0, page_size=10):
        pass

    def show_game_info(self, db_result):
        tmp_list_dict = defaultdict(dict)
        for i in db_result:
            if i['pkid'] in tmp_list_dict:
                tmp_list_dict[i['pkid']]['result'].append({
                    'player_id': i['player_id'],
                    'player_score': i['player_score']
                })
            else:
                tmp_list_dict[i['pkid']]['game_pkid'] = i['pkid']
                tmp_list_dict[i['pkid']]['game_id'] = i['game_id']
                tmp_list_dict[i['pkid']]['game_finish_datetime'] = i['game_finish_datetime']
                tmp_list_dict[i['pkid']]['score_to_money_rate'] = i['score_to_money_rate']
                tmp_list_dict[i['pkid']]['game_status'] = i['game_status']
                tmp_list_dict[i['pkid']]['result'] = [{'player_id': i['player_id'], 'player_score': i['player_score']}]
        result = sorted(tmp_list_dict.values(), key=lambda x: (-1 * x['game_status'], x['game_finish_datetime']), reverse=True)
        return result

    def get_data_by_date(self, game_type_pkid, user_pkid, start_dt, end_dt):
        db_result = GameInfoModel().get_data_by_date_with_result(game_type_pkid, user_pkid, start_dt, end_dt)
        result = []
        if len(db_result) == 0:
            return result
        return self.show_game_info(db_result)


    def get_all(self, game_type_pkid, user_pkid):
        db_result = GameInfoModel().get_all_with_result(game_type_pkid, user_pkid)
        result = []
        if len(db_result) == 0:
            return result
        return self.show_game_info(db_result)

    def check_game_result(self, game_type_pkid, game_id, score_to_money_rate, game_result_list):
        game_type_info = GameInfo().get_game_type_by_pkid(game_type_pkid)
        game_result_list = [g for g in game_result_list if g['player_id'] and g['player_score']]
        if not game_id:
            raise NormalError(output_message=u'没有填写房间ID')
        if not score_to_money_rate or not score_to_money_rate.isnumeric() or float(score_to_money_rate) <= 0:
            raise NormalError(output_message=u'分数金额比填写错误')
        if len(game_result_list) <= 1 or len(game_result_list) > game_type_info['most_player_count'] or len(set([g['player_id'] for g in game_result_list])) != len([g['player_id'] for g in game_result_list]):
            raise NormalError(output_message=u'玩家信息填写错误')
        if sum([float(g['player_score']) for g in game_result_list]) != 0.0:
            raise NormalError(output_message=u'玩家分数总数不为0')

    def create_one(self, game_type_pkid, user_pkid, game_id, score_to_money_rate, game_result_list):
        self.check_game_result(game_type_pkid, game_id, score_to_money_rate, game_result_list)
        exist_row = GameInfoModel().where({'game_id': game_id}).get_one()
        if exist_row:
            raise NormalError(output_message=u'房间ID已存在')
        with transaction_context:
            game_pkid = GameInfoModel().insert_one_row({
                'game_type_pkid': game_type_pkid,
                'user_pkid': user_pkid,
                'game_id': game_id,
                'score_to_money_rate': float(score_to_money_rate)
            })
            for result in game_result_list:
                GameResultModel().insert_one_row({
                    'game_type_pkid': game_type_pkid,
                    'user_pkid': user_pkid,
                    'player_id': result['player_id'],
                    'game_pkid': game_pkid,
                    'player_score': result['player_score']
                })

    def update_one(self, game_type_pkid, user_pkid, game_pkid, game_id, score_to_money_rate, game_finish_datetime, game_result_list):
        self.check_game_result(game_type_pkid, game_id, score_to_money_rate, game_result_list)
        with transaction_context:
            GameInfoModel().set_field({'score_to_money_rate': score_to_money_rate, 'game_id': game_id, 'game_finish_datetime': game_finish_datetime}).where({'pkid': game_pkid}).update()
            GameResultModel().delete_by_game_pkid(game_pkid)
            for result in game_result_list:
                GameResultModel().insert_one_row({
                    'game_type_pkid': game_type_pkid,
                    'user_pkid': user_pkid,
                    'player_id': result['player_id'],
                    'game_pkid': game_pkid,
                    'player_score': result['player_score']
                })

    def delete_one(self, game_pkid):
        with transaction_context:
            GameInfoModel().delete_one(game_pkid)
            GameResultModel().delete_by_game_pkid(game_pkid)
            GameCloseBillGameModel().delete_by_game_pkid(game_pkid)

    def get_game_type_by_pkid(self, game_type_pkid):
        return GameTypeModel().where({'pkid': game_type_pkid}).get_one()


class CloseBill(object):
    def __init__(self):
        pass

    def list_by_pagination(self, page_index, page_size):
        pass

    def output_close_bill_data(self, db_data):
        result = defaultdict(dict)
        for row in db_data:
            hid = row['history_pkid']
            if 'items' not in result[hid]:
                result[hid]['items'] = []
            result[hid]['items'].append({
                'player_id': row.pop('player_id'),
                'final_money': row.pop('final_money'),
                'money': row.pop('money'),
                'game_count': row.pop('game_count'),
                'fee': row.pop('fee')
            })
            result[hid].update(row)
        return sorted(result.values(), key=lambda x: x['close_bill_check_point'], reverse=True)

    def get_by_created_at(self, game_type_pkid, user_pkid, start_dt, end_dt):
        db_data = GameCloseBillHistoryModel().get_by_created_at_with_detail(game_type_pkid, user_pkid, start_dt, end_dt)
        return self.output_close_bill_data(db_data)

    def get_all(self, game_type_pkid, user_pkid):
        db_data = GameCloseBillHistoryModel().get_all_with_detail(game_type_pkid, user_pkid)
        return self.output_close_bill_data(db_data)

    def create_one(self, game_type_pkid, user_pkid, close_bill_check_point, fee_rate):
        fee_rate = float(fee_rate)
        game_list = GameInfoModel().select_field(['game_id', 'pkid', 'game_finish_datetime', 'score_to_money_rate']).where({'game_status': 0, 'game_type_pkid': game_type_pkid, 'user_pkid': user_pkid}).get_many()
        if len(game_list) == 0:
            raise NormalError(output_message=u'没有比赛需要结算')
        player_money = defaultdict(Counter)
        player_game_detail_row = []
        for game in game_list:
            result_list = GameResultModel().select_field(['player_id', 'player_score']).where({'game_pkid': game['pkid'], 'game_type_pkid': game_type_pkid, 'user_pkid': user_pkid}).get_many()
            for result in result_list:
                tmp_money = result['player_score'] * game['score_to_money_rate']
                player_money[result['player_id']]['money'] += tmp_money

                if result['player_score'] > 5:
                    tmp_fee = min(200, tmp_money * fee_rate * 1.0)
                    tmp_final_money = tmp_money - tmp_fee
                else:
                    tmp_fee = 0.0
                    tmp_final_money = tmp_money * 1.0

                player_money[result['player_id']]['final_money'] += tmp_final_money
                player_money[result['player_id']]['fee'] += tmp_fee

                player_game_detail_row.append({
                    'player_id': result['player_id'],
                    'player_score': result['player_score'],
                    'money': tmp_money,
                    'final_money': tmp_final_money,
                    'fee': tmp_fee,
                    'game_pkid': game['pkid'],
                    'game_id': game['game_id']
                })
                player_money[result['player_id']]['game_count'] += 1

        with transaction_context:
            pkid = GameCloseBillHistoryModel().insert_one_row({
                'close_bill_check_point': close_bill_check_point,
                'fee_rate': fee_rate,
                'total_final_money': sum([pm['final_money'] for pm in player_money.values()]),
                'total_money': sum([pm['money'] for pm in player_money.values()]),
                'total_fee': sum([pm['fee'] for pm in player_money.values()]),
                'total_game_count': len(game_list),
                'game_type_pkid': game_type_pkid,
                'user_pkid': user_pkid
            })
            for i in player_game_detail_row:
                i['history_pkid'] = pkid
                i['game_type_pkid'] = game_type_pkid
                i['user_pkid'] = user_pkid
            GameCloseBillGameModel().insert_many_row(player_game_detail_row)
            for k, v in player_money.items():
                GameCloseBillHistoryDetailModel().insert_one_row({
                    'player_id': k,
                    'final_money': v['final_money'],
                    'money': v['money'],
                    'fee': v['fee'],
                    'game_count': v['game_count'],
                    'history_pkid': pkid,
                    'game_type_pkid': game_type_pkid,
                    'user_pkid': user_pkid
                })
            GameInfoModel().set_field({'game_status': 1}).where({'pkid': [g['pkid'] for g in game_list]}).update()
        return pkid

    def delete_one(self, close_bill_history_pkid):
        with transaction_context:
            GameCloseBillHistoryModel().delete_one(close_bill_history_pkid)
            GameCloseBillHistoryDetailModel().delete_by_history_id(close_bill_history_pkid)
            GameCloseBillGameModel().set_status_game_id_by_close_history_pkid(close_bill_history_pkid, 0)
            GameCloseBillGameModel().delete_by_history_pkid(close_bill_history_pkid)

    def download_history_detail(self, game_type_pkid, user_pkid, close_bill_history_pkid):
        detail_data = GameCloseBillHistoryDetailModel().where({"history_pkid": close_bill_history_pkid, 'game_type_pkid': game_type_pkid, 'user_pkid': user_pkid}).get_many()
        csv_file = StringIO.StringIO()
        fieldname = ['玩家', '结账金额', '战绩金额', '比赛场次', '手续费']
        writer = csv.writer(csv_file)
        writer.writerow(fieldname)
        for row in detail_data:
            writer.writerow([row['player_id'].encode('utf8'), row['final_money'], row['money'], row['game_count'], row['fee']])
        return csv_file

    def get_close_bill_history_player_detail(self, game_type_pkid, user_pkid, player_id, history_pkid):
        return GameCloseBillGameModel().select_field(['player_id', 'game_id', 'game_pkid', 'final_money', 'money', 'fee', 'player_score']).where(
            {'player_id': player_id, 'history_pkid': history_pkid, 'game_type_pkid': game_type_pkid, 'user_pkid': user_pkid}
        ).get_many()


