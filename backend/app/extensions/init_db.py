#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# @Time    : 2024/2/4 16:03
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>


db = SQLAlchemy()


def init_db(app: Flask):
    db.init_app(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.username

    # 只有在 Werkzeug 主进程中才执行数据库初始化操作
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        with app.app_context():
            try:
                db.engine.connect()
                db.create_all()

            except Exception as e:
                exit(f"数据库连接失败: {e}")
