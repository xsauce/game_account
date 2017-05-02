# -*- coding: utf-8 -*-
import csv
import sys
from datetime import datetime
sys.path.append('/usr/local/game_account/')
from game_account.model import GameCloseBillHistoryDetailModel

from game_account.logic import GameInfo, CloseBill


def import_game_data(csv_file):
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print row
            GameInfo().create_one(row['game_id'], unicode(row['score_to_money_rate'], 'utf-8'), [
                {
                    'player_id': unicode(row['player1_id'], 'utf-8'),
                    'player_score': row['player1_score'],
                    'game_id': row['game_id']
                },
                {
                    'player_id': unicode(row['player2_id'], 'utf-8'),
                    'player_score': row['player2_score'],
                    'game_id': row['game_id']
                },
                {
                    'player_id': unicode(row['player3_id'], 'utf-8'),
                    'player_score': row['player3_score'],
                    'game_id': row['game_id']
                },
                {
                    'player_id': unicode(row['player4_id'], 'utf-8'),
                    'player_score': row['player4_score'],
                    'game_id': row['game_id']
                }
            ])

def close_bill(check_point, win_fee=0.05):
    check_point_dt = datetime.strptime(check_point, '%Y-%m-%dT%H:%M:%S')
    bill_pkid = CloseBill().create_one(check_point_dt, win_fee)
    with open('/Users/sam/Desktop/bill_%s.csv' % check_point.replace(' ', 'T'), 'w') as f:
        fields_name = ['player_id', 'final_money', 'money', 'fee', 'game_count']
        writer = csv.DictWriter(f, fieldnames=fields_name)
        writer.writeheader()

        result = GameCloseBillHistoryDetailModel().select_field(['player_id', 'final_money', 'money', 'fee', 'game_count']).where({'history_id': bill_pkid}).get_many()
        for i in result:
            writer.writerow({s: unicode(i[s]).encode("utf-8") for s in i})

if __name__ == '__main__':
    csv_file = sys.argv[1]
    # check_point = sys.argv[2]
    import_game_data(csv_file)
    # close_bill('2017-05-01T00:30:00')