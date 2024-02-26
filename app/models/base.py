#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/6 14:08                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

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
