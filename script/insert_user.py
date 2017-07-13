# -*- coding: utf-8 -*-
from util.tool_func import md5


def insert_user(user_name, password, expired_at, user_pkid, priv_item):
    sql = '''
    INSERT INTO game_account.game_user
    (pkid, username, password, created_at, updated_at, expired_at)
    VALUES(NULL, '%s', '%s', NOW(), '1970-01-01 00:00:00.000', '%s');
    ''' % (user_name, md5(password), expired_at)

    print sql

    for i in priv_item.split(','):
        print '''
        INSERT INTO game_account.game_user_priv
        (pkid, created_at, updated_at, user_pkid, priv_item, game_type_pkid)
        VALUES(NULL, NOW(), NOW(), %s, 'all', %s);
        ''' % (user_pkid, i)


insert_user('sample1', '123456', '2017-07-14 18:00:00', '2', '2')

