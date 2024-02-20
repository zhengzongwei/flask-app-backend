#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/18 17:40                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from flask import Blueprint, request

from app.models.book import Author
from app.schemas.books import AuthorSchema
from app.api.api import success_response, error_response
from app.common.utils.logs import Logger

from app.dao.authors import AuthorDao
from app.exceptions.authors import AuthorDeletionError, AuthorNotFound

logger = Logger('authors')

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/')
@bp.route('/<id>', methods=['GET'])
def authors(id=None):
    if id:
        author = AuthorDao().get_author_by_id(id)
        if not author:
            e = AuthorNotFound(author_id=id)
            return error_response(code=e.code, message=e.msg)
        return AuthorSchema().dump(author)
    else:
        data = AuthorDao().get_authors()
        authors_data = AuthorSchema(many=True).dump(data)
        return success_response(data=authors_data)


@bp.route('/', methods=['DELETE'])
def delete_author():
    authors = AuthorSchema().validate_delete_author_data(request.json)
    try:
        AuthorDao.delete_author(authors)
    except AuthorDeletionError as e:
        return error_response(e.code, e.message)
    return success_response()


@bp.route('/<id>', methods=['PUT'])
def update_author(id):
    book = AuthorSchema().load(request.json['book'])
    try:
        AuthorDao.update_author(id, book)
    except AuthorNotFound as e:
        return error_response(code=e.code, message=e.msg)
    return success_response()
