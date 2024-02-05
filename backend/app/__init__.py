#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/4 15:33                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

import os
from flask import Flask

from conf.conf import config as config
from extensions import init_plugs


def create_app(conf=None):
    app = Flask(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    # app = Flask(__name__, instance_relative_config=True)

    # 加载配置
    app.config.from_object(config.get(conf))

    # 注册插件
    init_plugs(app)

    # 注册蓝图

    # 注册命令

    return app
