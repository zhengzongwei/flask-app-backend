#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/4 15:33                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

import os
from flask import Flask

from app.api import init_bps
from app.conf.conf import config as config
from app.extensions import init_plugs
from flask_babel import Babel


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                               'translations')

    try:
        os.makedirs(os.path.join(os.path.dirname(app.root_path), 'logs'), exist_ok=True)
    except OSError:
        pass
    # 加载配置
    FLASK_ENV = os.environ.get('FLASK_ENV')
    if FLASK_ENV is None or FLASK_ENV not in ['development', 'production','testing']:
        app.config.from_object(config['development'])
    else:
        app.config.from_object(config[FLASK_ENV])
    # if app.debug:
    #     app.config.from_object(config['development'])
    # else:
    #     app.config.from_object(config['production'])

    # 注册插件
    init_plugs(app)

    # 注册蓝图
    init_bps(app)

    # 注册命令

    return app
