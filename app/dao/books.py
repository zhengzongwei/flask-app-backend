#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/18 10:45
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from datetime import datetime

from app.extensions import db
from app.models.book import Author, Book
from app.schemas.books import BookSchema
from app.dao.authors import AuthorDao
from app.exceptions import exceptions

class BookDao(object):

    @staticmethod
    def list_book(offset=0, limit=10):
        return Book.query.filter_by(is_deleted=False).offset(offset).limit(limit).all()

    @staticmethod
    def create_book(books):
        author_dao = AuthorDao()
        try:
            for book in books:
                authors = author_dao.create_author(book.authors)
                book.authors = authors
            db.session.add_all(books)
            db.session.commit()
        except exceptions.BookCreateException as e:
            db.session.rollback()
            raise exceptions.BookCreateException(str(e))

    @staticmethod
    def delete_book(book_ids):
        try:
            # 检查书籍是否存在
            for book_id in book_ids:
                book = Book.query.filter_by(id=book_id).first()
                if book:
                    book.authors.clear()
                    book.is_delete = 1
                    book.deleted_at = datetime.now()
        except Exception as e:
            db.session.rollback()
            raise exceptions.BookDeleteException(e)
        db.session.commit()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.filter_by(id=book_id, is_deleted=False).first()

    @staticmethod
    def get_book_by_name(name):
        return Book.query.filter_by(name=name, is_deleted=False).first()
