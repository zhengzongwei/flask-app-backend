#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 11:33                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask import Blueprint, request

from app.models.book import Book
from app.schemas.books import BookSchema
from app.api.api import success_response, error_response
from app.common.utils.logs import Logger

from app.dao.books import BookDao

logger = Logger('books')

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/')
@bp.route('/<id>', methods=['GET'])
def books(id=None):
    # 获取查询参数
    name = request.args.get('name')

    if id:
        book = Book.get_by_id(id)
    elif name:
        book = Book.get_by_name(name)
    else:
        data = Book.query.filter_by(is_deleted=False).all()
        books_data = BookSchema(many=True).dump(data)
        return success_response(data=books_data)

    # 执行查询
    if not book:
        return error_response('Book not found', 404)
    return BookSchema().dump(book)


@bp.route('/', methods=['POST'])
def add_book():
    books = BookSchema().load(request.json['books'], many=True)
    BookDao.create_book(books)
    return success_response()


@bp.route('/', methods=['DELETE'])
def delete_book():
    books = BookSchema().validate_delete_book_data(request.json)
    BookDao.delete_book(books)
    return success_response()
