#!/usr/bin/python
# -*- coding: utf-8 -*-
## Copyright (c) 2017-2018, The Sumokoin Project (www.sumokoin.org)
## Copyright (c) 2018, The Fonero Project (www.fonero.org)
'''
App top-level settings
'''

__doc__ = 'default application wide settings'

import sys
import os
import logging

from utils.common import getHomeDir, makeDir

USER_AGENT = "Fonero GUI Wallet"
APP_NAME = "Fonero GUI Wallet"
VERSION = [1, 3, 0, 1]


_data_dir = makeDir(os.path.join(getHomeDir(), 'FoneroGUIWallet'))
DATA_DIR = _data_dir

log_file  = os.path.join(DATA_DIR, 'logs', 'app.log') # default logging file
log_level = logging.DEBUG # logging level

seed_languages = [("1", "English"), 
                  ("2", "Spanish"), 
                  ("0", "German"), 
                  ("4", "Italian"), 
                  ("6", "Portuguese"),
                  ("7", "Russian"),
                  ("8", "Japanese"),
                ]

# COIN - number of smallest units in one coin
COIN = 1000000000000.0

WALLET_RPC_HOST = "127.0.0.1"
WALLET_RPC_PORT = 18182
REMOTE_DAEMON_HOST = "node.fonero.org"
REMOTE_DAEMON_PORT = 18181

RESOURCES_PATH = "../Resources" if sys.platform == 'darwin' and hasattr(sys, 'frozen') else "./Resources"
