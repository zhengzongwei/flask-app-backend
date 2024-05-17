#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

import os

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.query import Query as BaseQuery


db = SQLAlchemy()
ma = Marshmallow()


def init_db(app: Flask):
    db.init_app(app)
    ma.init_app(app)

    # 只有在 Werkzeug 主进程中才执行数据库初始化操作
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        with app.app_context():
            try:
                db.engine.connect()

            except Exception as e:
                exit(f"数据库连接失败: {e}")
