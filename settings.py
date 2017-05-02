# -*- coding: utf-8 -*-
import os

DATABASES = {
    "game_account": {
        "NAME": "game_account",
        "HOST": "127.0.0.1",
        "USER": "game_account",
        "PASSWORD": "game_account",
        "PORT": 3306,
        "TYPE": "mysql"
    }
}

TORNADO_LOG_SETTINGS = {
    'logging': 'debug',  # debug|info|warning|error|none
    'log_to_stderr': True,  # True|False
    'log_file_prefix': '/var/log/game_account',
    'log_file_max_size': 100 * 1000 * 1000,
    'log_file_num_backups': 50,
    'log_rotate_when': 'midnight',  # S|M|H|D|W0-W6
    'log_rotate_interval': 1,
    'log_rotate_mode': 'time',  # size|time
    'log_fmt': '%(levelname)1.1s\t%(process)s\t%(asctime)s\t%(message)s',
    'log_datefmt': None
}

TORNADO_SERVER_SETTINGS = {
    'ip': '0.0.0.0',
    'port': '10080',
    'async_max_http_client': 50,
    'async_request_max_wait_seconds': 5,
    'subprocess_num': 0,
    'multi_mode': False,
    'wait_seconds_before_shutdown': 10
}


TORNADO_APPLICATION_SETTINGS = {
    'debug': True
}

ROOT_DIR = '/usr/local/game_account'