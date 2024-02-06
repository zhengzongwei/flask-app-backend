#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 19:17                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
import datetime
from app.extensions import db


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="Book ID")
    name = db.Column(db.String(255), nullable=False, comment="Book Name")
    author = db.Column(db.String(255), nullable=False, comment="Book Author")
    publication_date = db.Column(db.Date, nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False, comment="ISBN")
    created_at = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False, comment="Book Creation Date")
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False,
                           onupdate=datetime.datetime.now, comment="Book Creation Date")
    deleted_at = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False,
                           onupdate=datetime.datetime.now, comment="Book Delete Date")
