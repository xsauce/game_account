# -*- coding: utf-8 -*-
import os


ROOT_DIR = '/usr/local/game_account'

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
    'debug': True,
    'static_path': os.path.join(ROOT_DIR, 'game_account', 'static'),
    'cookie_secret': u"\x81\xb5\r%\x98\xfd`\xc6\xd63\xab\xfb\xf9\xbd?\xbd\x1e\xe7O\xaf\x88\x189\x1f (\xca0\xa4\x16\xa4\x8b\xd8\x92\x9c+e\x9d\x9bT\xf63\xfc`\xf3\xb4Z\xa5P\xaci\x86b\xbf\xe3\xdb\x1d\x97\xcb\xa6M!\x19\x87\xfa\x8e\x94\x03\xea\x05b;\xce\x89A\xbd\x81\x82\xe7\xc5S\xb2\xdc\xbf+\x19\x1d\xe8\x03}\x12|\x18U}\xbf\x84\xcb\x9c\xe5~s`r\x9d\xef7.9\xce\x9b\xd8\xb7~D\x9e\xb0\x87\xda\x0ex}S\xca\rupZD\xcd\xb2\xf2\x08,l\xb5tS\x10\x9buurv\xcc\xec\xee\xcbC\x9a\x08 \x8d?\r\x9b\x9f\x84\xc7\xb2:\xeb'6\xfb\x93\xf3>^\xe7\xe3\xdf\x9aR*\x99\xc82j\xd6z*>\xb9(\xf6\x97T?\xb1\xf3W\x021\xd7\x17\t\xc0\xa2\xe4\xba\xd2'\xeaDl\xfe\xe4OP\xf6\x14\x9c\x91\x1c\x8e\x19'@$\rs\x8al\xd4\x1e\x87u\xd6\x875O\xd4sg\x92\xf5\x89\xae\x1a\x18+c\xd8\xc8\x7fL\x86k\xe6'\xff-\xe3\xf7\xcf"
}

