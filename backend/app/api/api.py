#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 14:06                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
import datetime

from flask import Blueprint, jsonify, request
from flask_babel import _

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/')
def api_info():
    data = {
        "api_version": 'v1',
    }

    return success_response(data)


def success_response(data=None, status_code=200, message=None):
    """
    创建一个成功的 JSON 格式响应
    """
    response = {
        # "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "code": 0,
        "message": message,
        "data": data
    }
    return jsonify(response), status_code


def error_response(code=-1, status_code=500, message=None):
    """
    创建一个错误的 JSON 格式响应
    """
    response = {
        "code": code,
        "message": message,
    }
    return jsonify(response), status_code
