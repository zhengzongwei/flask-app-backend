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
        author = Author.query.filter_by(id=id, is_deleted=False).first()
        if not author:
            exception = AuthorNotFound(author_id=id)
            return error_response(code=exception.code, message=exception.msg)
            # raise AuthorNotFound(author_id=id)
        return AuthorSchema().dump(author)
    else:
        data = Author.query.filter_by(is_deleted=False).all()
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
