#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/18 14:52                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from flask import Blueprint

from .books import bp as book_bp

books_bp = Blueprint('books', __name__, url_prefix='/books')


def init_book_bps(app) -> None:
    books_bp.register_blueprint(book_bp)

