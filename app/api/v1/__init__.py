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

from .auhtors.authors import bp as authors_bp
from .books.books import bp as books_bp

v1_prefix = 'v1'
v1_bp = Blueprint(v1_prefix, __name__, url_prefix=f'{v1_prefix}')
v1_bp.register_blueprint(authors_bp)
v1_bp.register_blueprint(books_bp)
