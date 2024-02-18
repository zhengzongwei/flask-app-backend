#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/4 16:00                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask import Flask, Blueprint
from app.api.api import bp as api_bp
from app.api.v1 import v1_bp,init_v1_bps
apis_bp = Blueprint('api', __name__, url_prefix='/api')


def register_api_blueprint(app: Flask) -> None:
    apis_bp.register_blueprint(v1_bp)
    apis_bp.register_blueprint(api_bp)
    app.register_blueprint(apis_bp)


def init_bps(app: Flask) -> None:
    init_v1_bps(app)
    register_api_blueprint(app)

