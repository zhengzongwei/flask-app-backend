#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/5 11:33                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask import Blueprint, jsonify

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/')
def books_info():
    return jsonify("Hello World")
