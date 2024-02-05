#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/5 11:09                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask import Flask
from .init_db import init_db


def init_plugs(app: Flask) -> None:
    init_db(app)
