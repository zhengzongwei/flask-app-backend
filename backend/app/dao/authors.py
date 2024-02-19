#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/19 10:13                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from app.models.book import Author
from app.extensions import db
from app.exceptions.authors import AuthorNotFound, AuthorDeletionError, AuthorCreationError, AuthorAlreadyExists


class AuthorDao(object):

    @staticmethod
    def create_author(authors):
        pass

    @staticmethod
    def delete_author(author_ids):
        pass

        try:
            for author_id in author_ids:
                author = Author.query.filter_by(id=author_id).first()
                if author or author.books:
                    # 检查是否有关联的书籍，如果有关联的书籍，不允许删除
                    raise AuthorDeletionError(author_id=author_id)
        except AuthorDeletionError:
            db.session.rollback()
