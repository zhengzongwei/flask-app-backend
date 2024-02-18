#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/18 17:39                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from flask import Blueprint

from .authors import bp as author_bp

authors_bp = Blueprint('authors',__name__,url_prefix='/authors')


def init_author_bps(app) -> None:
    authors_bp.register_blueprint(author_bp)
