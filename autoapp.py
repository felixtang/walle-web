# -*- coding: utf-8 -*-
"""Create an application instance."""
import sys

from flask.helpers import get_debug_flag
from walle.app import create_app
from walle.config.settings import DevConfig, TestConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag(default=True) else ProdConfig

if 2 in sys.argv and sys.argv[2] == 'test':
    CONFIG = TestConfig

app = create_app(CONFIG)
