#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/5 11:33                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask import Blueprint, request
from marshmallow import ValidationError

from app.models.books.book import Book
from app.schemas.books import BookSchema
from app.api.api import success_response, error_response
from app.extensions import db
from app.common.utils.logs import Logger

logger = Logger('books')

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/')
def books():
    data = Book.query.all()
    books_data = BookSchema(many=True).dump(data)
    return success_response(data=books_data)


@bp.route('/add', methods=['POST'])
def add_book():
    params = request.json

    try:
        books = BookSchema(many=True).load(params['books'])
        logger.debug("books")
        db.session.add_all(books)
        db.session.commit()

    except ValidationError as err:
        logger.debug(err)
        db.session.rollback()
        return error_response(err.messages), 400
    return success_response()
