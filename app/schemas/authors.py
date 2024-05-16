#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/18 17:38                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from app.models.book import Author
from flask_babel import _
from app.common.utils.logs import Logger
from app.extensions import ma

logger = Logger("AuthorSchema")


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    # name = fields.String(required=True)
    class Meta:
        model = Author
        include_fk = True
        load_instance = True
        exclude = ("deleted_at",)
