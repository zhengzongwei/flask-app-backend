#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 19:17                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
import datetime

from sqlalchemy import ForeignKey
from app.extensions import db
from app.models.base import BaseModel
from sqlalchemy.orm import relationship


class Book(BaseModel, db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="Book ID")
    name = db.Column(db.String(255), nullable=False, comment="Book Name")
    count_page = db.Column(db.String(10), comment="Book Count Page")
    publication_date = db.Column(db.Date)
    isbn = db.Column(db.String(20), unique=True, comment="ISBN")
    version = db.Column(db.String(10), comment="Book Version")
    url = db.Column(db.String(50), comment="Book URL")
    is_delete = db.Column(db.Boolean, default=False)
    authors = relationship("Author", secondary="book_m2m_author", back_populates='books')
    # publisher = relationship("Publish", secondary="book_m2m_publish", back_populates='book_id')


class Author(BaseModel, db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    phone = db.Column(db.String(11))
    addr = db.Column(db.String(80))
    books = relationship("Book", secondary="book_m2m_author", back_populates="authors")


class Book_m2m_author(BaseModel, db.Model):
    __tablename__ = "book_m2m_author"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, ForeignKey("books.id"))
    author_id = db.Column(db.Integer, ForeignKey("authors.id"))
