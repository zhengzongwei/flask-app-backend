#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/19 10:13                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from app.models.book import Author
from app.extensions import db
from app.exceptions.authors import AuthorNotFound, AuthorDeletionError, AuthorCreationError, AuthorAlreadyExists


def get_author_by_name(name):
    return Author.query.filter_by(name=name, is_deleted=False).first()


class AuthorDao(object):

    @staticmethod
    def get_author_by_id(id):
        return Author.query.filter_by(id=id, is_deleted=False).first()

    @staticmethod
    def get_author_by_name(name):
        return Author.query.filter_by(name=name, is_deleted=False).first()

    def create_author(self, author):
        _author = self.get_author_by_name(author.name)
        if _author:
            raise AuthorAlreadyExists(author_id=_author.id)
        new_author = Author(name=author.name)
        db.session.add(new_author)
        db.session.commit()
        return new_author

    def create_authors(self, authors):
        for author in authors:
            self.create_author(author)

    def delete_author(self, author_ids):
        try:
            for author_id in author_ids:
                author = self.get_author_by_id(author_id)
                if author or author.books:
                    # 检查是否有关联的书籍，如果有关联的书籍，不允许删除
                    raise AuthorDeletionError(author_id=author_id)
        except AuthorDeletionError:
            db.session.rollback()
