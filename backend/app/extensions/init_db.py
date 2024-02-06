#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.query import Query as BaseQuery

# @Time    : 2024/2/4 16:03
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>


db = SQLAlchemy()
ma = Marshmallow()


def init_db(app: Flask):
    db.init_app(app)
    ma.init_app(app)

    # 只有在 Werkzeug 主进程中才执行数据库初始化操作
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        with app.app_context():
            try:
                db.engine.connect()

            except Exception as e:
                exit(f"数据库连接失败: {e}")
