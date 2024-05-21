#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

from flask import Blueprint, request

from app.models.book import Book
from app.schemas.books import BookSchema
from app.api.api import success_response, error_response
from app.common.utils.logs import Logger

from app.dao.books import BookDao
from . import books_bp as bp

logger = Logger('books')


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
