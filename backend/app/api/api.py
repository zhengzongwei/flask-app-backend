#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 14:06                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask import Blueprint, jsonify, request

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/')
def api_info():
    return jsonify("VVVV1111111")
