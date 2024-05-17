#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

from flask import Flask

from .init_db import init_db, db, ma
from .init_i18n import init_i18n
from .init_migrate import init_migrate


def init_plugs(app: Flask) -> None:
    init_db(app)
    init_i18n(app)
    init_migrate(app)
