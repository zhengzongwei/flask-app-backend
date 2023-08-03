from flask import jsonify, request

from . import books as api

from app.models.book import Books, Author, Publish
from app.common.db import db

data = {"code": 0, "msg": 'success', 'data': []}


@api.route('/', methods=['GET'])
def books():
    books_info = Books.query.all()
    if books:
        for book in books_info:
            data['data'].append(book.to_json())
    return data


@api.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Books.query.filter(Books.id == book_id).first()
    data['data'].append(book.to_json())
    return data


@api.route('/', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if 'books' in request_data:
        add_book = []
        for book_info in request_data['books']:
            book = Books()
            if not book_info['author']:
                return {
                    'code': -1,
                    'msg': "参数校验不通过，缺失 books"
                }

            add_authors = []
            for _author in book_info['author']:
                author_info = Author.query.filter(Author.name == _author).first()
                if author_info is None:
                    add_authors.append(Author(name=_author))
            book.author = add_authors

            if not book_info['publisher']:
                return {
                    'code': -1,
                    'msg': f"参数校验不通过，缺失 publisher"
                }

            add_publisher = []
            for _publisher in book_info['publisher']:
                publisher = Publish.query.filter(Publish.name == _publisher).first()
                if publisher is None:
                    add_publisher.append(Publish(name=_publisher))
            book.publisher = add_publisher

            if not book_info['name']:
                return {
                    'code': -1,
                    'msg': "参数校验不通过，缺失 name"
                }

            _book = Books.query.filter(Books.name == book_info['name']).first()
            if _book is not None:
                return {
                    'code': 1001,
                    'msg': f"书籍 {book_info['name']} 已存在"
                }
            book.name = book_info['name']
            add_book.append(book)

        try:
            db.session.add_all(add_book)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            data['code'] = 1001
            data['message'] = "数据保存失败,err=%s" % e
    return data


# @api.route('/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     request_data = request.get_json()
#
#     book = Books.query.filter(Books.id == book_id).update(name=request_data.get('name'))
#     print(book)
#     return data


@api.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Books.query.filter(Books.id == book_id).update({"is_delete": True})
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        data['code'] = 1001
        data['message'] = "数据保存失败,err=%s" % e
    return data
