# -*- coding: utf-8 -*-
from collections import defaultdict

from util.base_model import BaseModel


class UserModel(BaseModel):
    _TABLE = 'game_user'
    def __init__(self):
        super(UserModel, self).__init__()

class SessionModel(BaseModel):
    _TABLE = 'game_session'

    def __init__(self):
        super(SessionModel, self).__init__()

class UserPrivModel(BaseModel):
    _TABLE = 'game_user_priv'

    def __init__(self):
        super(UserPrivModel, self).__init__()

    def get_game_type_user_priv_list(self, user_pkid, game_type_pkid):
        priv_items = UserPrivModel().select_field(['priv_item']).where({'user_pkid': user_pkid, 'game_type_pkid': game_type_pkid}).get_many()
        return [i['priv_item'] for i in priv_items]