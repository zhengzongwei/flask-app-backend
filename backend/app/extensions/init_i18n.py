#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 16:25                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask_babel import Babel


def init_i18n(app):
    babel = Babel(app)
