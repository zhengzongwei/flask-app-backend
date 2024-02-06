#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 19:17                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
import datetime
from app.extensions import db

from app.models.base import BaseModel


class Book(BaseModel, db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="Book ID")
    name = db.Column(db.String(255), nullable=False, comment="Book Name")
    author = db.Column(db.String(255), nullable=False, comment="Book Author")
    publication_date = db.Column(db.Date)
    isbn = db.Column(db.String(20), unique=True, comment="ISBN")

