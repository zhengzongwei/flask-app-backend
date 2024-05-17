#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/18 17:40                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from flask import Blueprint, request

from app.models.book import Author
from app.schemas.books import AuthorSchema
from app.api.api import success_response, error_response
from app.common.utils.logs import Logger

from app.dao.books import BookDao

logger = Logger('authors')

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/')
@bp.route('/<id>', methods=['GET'])
def authors(id=None):
    if id:
        book = Author.query.filter_by(id=id, is_deleted=False).first()
        if not book:
            return error_response('Author not found', 404)
        return AuthorSchema().dump(book)
    else:
        data = Author.query.filter_by(is_deleted=False).all()
        authors_data = AuthorSchema(many=True).dump(data)
        return success_response(data=authors_data)

@bp.route('/', methods=['POST'])
def create_author():
    pass