#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/4 15:33                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

import os
from flask import Flask

from api import init_bps
from conf.conf import config as config
from extensions import init_plugs


def create_app(conf=None):
    app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(os.path.join(os.path.dirname(app.root_path),'logs'), exist_ok=True)
    except OSError:
        pass
    # 加载配置
    app.config.from_object(config.get(conf))

    # 注册插件
    init_plugs(app)

    # 注册蓝图
    init_bps(app)

    # 注册命令

    return app
