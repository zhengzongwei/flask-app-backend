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
from app.exceptions.books import BookNotFound, BookAlreadyExists, BookDeletionError

logger = Logger('books')

bp = Blueprint('/', __name__, url_prefix='/')


@bp.route('/')
@bp.route('/<id>', methods=['GET'])
def books(id=None):
    if id:
        book = BookDao().get_book_by_id(id)
        if not book:
            e = BookNotFound(book_id=id)
            return error_response(code=e.code, message=e.message)
        return BookSchema().dump(book)
    else:
        data = BookDao.get_books()
        books_data = BookSchema(many=True).dump(data)
        return success_response(data=books_data)


@bp.route('/', methods=['POST'])
def add_book():
    books = BookSchema().load(request.json['books'], many=True)
    try:
        BookDao.create_books(books)
    except BookAlreadyExists as e:
        return error_response(code=e.code, message=e.msg)
    return success_response()


@bp.route('/', methods=['DELETE'])
def delete_book():
    books = BookSchema().validate_delete_book_data(request.json)
    try:
        BookDao.delete_book(books)
    except (BookDeletionError, BookNotFound) as e:
        return error_response(code=e.code, message=e.msg)
    return success_response()


@bp.route('/<id>', methods=['PUT'])
def update_book(id):
    book = BookSchema().load(request.json['book'])
    try:
        BookDao.update_book(id, book)
    except BookNotFound as e:
        return error_response(code=e.code, message=e.msg)
    return success_response()
