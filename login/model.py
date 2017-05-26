# -*- coding: utf-8 -*-
from util.base_model import BaseModel


class UserModel(BaseModel):
    _TABLE = 'game_user'
    def __init__(self):
        super(UserModel, self).__init__()

class SessionModel(BaseModel):
    _TABLE = 'game_session'

    def __init__(self):
        super(SessionModel, self).__init__()
