#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/5 11:09                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask import Flask

from .init_db import init_db, db
from .init_i18n import init_i18n
from .init_migrate import init_migrate

def init_plugs(app: Flask) -> None:
    init_db(app)
    init_i18n(app)
    init_migrate(app)
