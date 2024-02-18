#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/18 10:45                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from datetime import datetime

from app.extensions import db
from models.book import Author, Book


class BookDao(object):

    @staticmethod
    def create_book(books):
        for book in books:
            authors = []
            for author in book.authors:
                author_name = author.name
                existing_author = Author.query.filter_by(name=author_name).first()
                if existing_author:
                    authors.append(existing_author)
                else:
                    new_author = Author(name=author_name)
                    db.session.add(new_author)
                    authors(new_author)
                book.authors = authors
        db.session.add_all(books)
        db.session.commit()

    @staticmethod
    def delete_book(book_ids):
        try:
            # 检查书籍是否存在
            for book_id in book_ids:
                book = Book.query.filter_by(id=book_id).first()
                if book:
                    book.authors.clear()
                    # db.session.delete(book)
                    book.is_delete = 1
                    book.deleted_at = datetime.now()
            db.session.commit()
        except Exception as e:
            db.session.rollback()




