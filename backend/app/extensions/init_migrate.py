#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/6 10:32                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask import Flask
from flask_migrate import Migrate
from .init_db import db
from app.models import *

migrate = Migrate()


def init_migrate(app: Flask) -> None:
    migrate.init_app(app, db)
