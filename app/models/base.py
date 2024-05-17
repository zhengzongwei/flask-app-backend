#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

import datetime
from app.extensions.init_db import db


class BaseModel(object):
    """
    模型基类，为每个模型补充创建时间和更新时间
    """
    created_at = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False, comment="Create Time")
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now,
                           comment="Update Time")
    deleted_at = db.Column(db.DateTime, default=None, comment="Delete Date")
