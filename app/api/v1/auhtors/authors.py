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

from app.dao.authors import AuthorDao
from app.models.book import Author
from app.schemas.books import AuthorSchema
from app.api.api import success_response, error_response

from app.common.utils.logs import Logger

from app.dao.books import BookDao
from . import authors_bp as bp

logger = Logger('authors')


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
    data = request.json
    create_many = False
    if isinstance(data, list):
        create_many = True

    _authors = AuthorSchema.load(request.json['authors'], many=create_many)
    AuthorDao.create_author(_authors)
    return success_response('Author created', 201)


@bp.route('/', methods=['DELETE'])
def delete_author():
    pass


@bp.route('/<id>', methods=['PUT'])
def edit_author(id=None):
    author = AuthorSchema.load(request.get_json(), partial=True)
    AuthorDao.edit_author(id, author)
    return success_response('Author edited', 204)
