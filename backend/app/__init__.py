#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/4 15:33                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

import os
from flask import Flask
from conf.conf import config as conf


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config.from_pyfile('conf.py', silent=True)
    else:
        app.config.from_object(conf.get(config, 'development'))

    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        pass

    return app


if __name__ == '__main__':
    import os

    environment = os.getenv('FLASK_ENV', 'development')

    # 创建 Flask 应用程序
    app = create_app(environment)

    # 在这里可以添加额外的配置，如端口号等

    # 运行 Flask 应用程序
    app.run()
