#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/18 10:45                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from datetime import datetime

from app.extensions import db
from app.models.book import Author, Book
from app.exceptions.books import BookDeletionError, BookCreationError, BookAlreadyExists, BookNotFound
from app.common.utils.logs import Logger
from app.dao.authors import AuthorDao

logger = Logger("BookDao")


class BookDao(object):

    @staticmethod
    def get_books():
        return Book.query.filter_by(is_deleted=False).all()

    @staticmethod
    def get_book_by_id(id):
        return Book.query.filter_by(id=id).first()

    @staticmethod
    def get_book_by_name(name):
        return Book.query.filter_by(name=name).first()

    def create_book(self, book):
        _book = self.get_book_by_name(book.name)
        if _book:
            raise BookAlreadyExists(book_name=_book.name)
        authors = []
        for author in book.authors:
            existing_author = AuthorDao.get_author_by_name(author.name)
            if existing_author:
                authors.append(existing_author)
            else:
                new_author = AuthorDao.create_author(author)
                authors.append(new_author)
            book.authors = authors
        db.session.add(book)
        db.session.commit()

    def create_books(self, books):
        for book in books:
            self.create_book(book)
        #     authors = []
        #     book_name = book.name
        #     existing_book = Book.query.filter_by(name=book_name).first()
        #     if existing_book:
        #         raise BookAlreadyExists(book_name=book_name)
        #
        #     for author in book.authors:
        #         author_name = author.name
        #         existing_author = Author.query.filter_by(name=author_name).first()
        #         if existing_author:
        #             authors.append(existing_author)
        #         else:
        #             new_author = Author(name=author_name)
        #             db.session.add(new_author)
        #             authors.append(new_author)
        #         book.authors = authors
        # db.session.add_all(books)
        # db.session.commit()

    def delete_book(self, book_ids):
        try:
            # 检查书籍是否存在
            for book_id in book_ids:
                book = self.get_book_by_id(book_id)
                if not book:
                    raise BookNotFound(book_id=book_id)
                book.authors.clear()
                # db.session.delete(book)
                book.is_delete = 1
                book.deleted_at = datetime.now()
            db.session.commit()
        except BookDeletionError:
            db.session.rollback()

    def update_book(self, id, book):
        logger.info(f"Update book {book.name}")
        db_book = self.get_book_by_id(id)
        if not book:
            raise BookNotFound(book_id=id)
        # 是否需要特殊处理
        db_book.name = book.name
        db_book.isbn = book.isbn
        db_book.version = book.version

        existing_author = [author.name for author in db_book.authors]
        # 删除作者
        for db_author in db_book.authors:
            if db_author.name not in [author.name for author in book.authors]:
                db_book.authors.remove(db_author)

        for author in book.authors:
            if author.name not in existing_author:
                # 检测作者是否已存在，如果存在 只需要添加关联关系
                existing_db_author = AuthorDao.get_author_by_name(author.name)
                if not existing_db_author:
                    new_author = AuthorDao.create_author(author)
                    # new_author = Author(name=author.name)
                    # db.session.add(new_author)
                    # db.session.commit()
                    db_book.authors.append(new_author)
                else:
                    db_book.authors.append(existing_db_author)

        # 提交更改到数据库
        db.session.commit()
