#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 11:33                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from flask import Blueprint

from .books import init_book_bps, books_bp
from .auhtors import init_author_bps, authors_bp

v1_bp = Blueprint('v1', __name__, url_prefix='/v1')


def init_v1_bps(app) -> None:
    init_book_bps(app)
    init_author_bps(app)
    v1_bp.register_blueprint(authors_bp)
    v1_bp.register_blueprint(books_bp)
