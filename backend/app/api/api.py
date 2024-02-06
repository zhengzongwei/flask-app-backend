#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 14:06                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
import datetime

from flask import Blueprint, jsonify, request
from flask_babel import _
from app.exception_error.exception_code import exception_code
bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/')
def api_info():
    data = {
            "api_version": 'v1',
    }

    return success_response(data)


def success_response(data=None, code=0, status_code=200):
    """
    创建一个成功的 JSON 格式响应
    """
    response = {
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "code": code,
        "message": _(exception_code.get(code)),
        "data": data
    }
    return jsonify(response), status_code


def error_response(code=-1, status_code=500):
    """
    创建一个错误的 JSON 格式响应
    """
    response = {
        "code": "exception_error",
        "message": _(exception_code.get(code)),
    }
    return jsonify(response), status_code
