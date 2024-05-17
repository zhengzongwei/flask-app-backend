#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

from flask import Flask, Blueprint
from app.api.api import bp as api_bp
from app.api.v1 import v1_bp, init_v1_bps

apis_bp = Blueprint('api', __name__, url_prefix='/api')


def register_api_blueprint(app: Flask) -> None:
    apis_bp.register_blueprint(v1_bp)
    apis_bp.register_blueprint(api_bp)
    app.register_blueprint(apis_bp)


def init_bps(app: Flask) -> None:
    init_v1_bps(app)
    register_api_blueprint(app)
