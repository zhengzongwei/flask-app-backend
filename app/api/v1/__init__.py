#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

from flask import Blueprint

from .books import init_book_bps, books_bp
from .auhtors import init_author_bps, authors_bp

v1_bp = Blueprint('v1', __name__, url_prefix='/v1')


def init_v1_bps(app) -> None:
    init_book_bps(app)
    init_author_bps(app)
    v1_bp.register_blueprint(authors_bp)
    v1_bp.register_blueprint(books_bp)
