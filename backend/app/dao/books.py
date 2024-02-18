#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/18 10:45                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from app.extensions import db
from app.models.books.book import Author


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

