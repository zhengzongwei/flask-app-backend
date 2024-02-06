#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/6 10:29                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from app.models.books.book import Book


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        # 自动加载到实例对象中
        load_instance = True
