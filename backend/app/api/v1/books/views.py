from flask import jsonify, request

from . import books as api
from app.common.logs import Logger
from flask_babel import gettext as _
from app.models.book import Books, Author, Publish
from app.common.common import db
from app.schema.book import BookSchema
from app.utils.code import Code

LOG = Logger("book")

data = {"code": 0, "msg": _("Success")}


@api.route('/', methods=['GET'])
def books():
    data['data'] = list()
    books_info = Books.query.all()
    if books:
        for book in books_info:
            data['data'].append(book.to_json())
    return data


@api.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    data['data'] = list()
    data['msg'] = _("Success")
    book = Books.query.filter(Books.id == book_id).first()
    data['data'].append(book.to_json())
    return data


@api.route('/', methods=['POST'])
def add_book():
    request_data = request.get_json()
    LOG.debug(f'the request_data {request_data}')
    book_schema = BookSchema()
    data = book_schema.load(request_data['books'], many=True)
    LOG.debug(f'the data {data}')
    if 'books' in request_data:
        add_book = []
        for book_info in request_data['books']:
            book = Books()
            if not book_info['author']:
                return {
                    'code': -1,
                    'msg': "参数校验不通过，缺失 books"
                }

            for _author in book_info['author']:
                author_info = Author.query.filter(Author.name == _author).first()
                if author_info is None:
                    book.author.append(Author(name=_author))
                else:
                    book.author.append(author_info)

            if not book_info['publisher']:
                return {
                    'code': -1,
                    'msg': f"参数校验不通过，缺失 publisher"
                }

            for _publisher in book_info['publisher']:
                publisher = Publish.query.filter(Publish.name == _publisher).first()
                if publisher is None:
                    book.publisher.append(Publish(name=_publisher))
                else:
                    book.publisher.append(publisher)

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


@api.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    request_data = request.get_json()
    print(request_data)
    book_schema = BookSchema()
    data = book_schema.load(request_data['books'])
    LOG.info(f"the schema data {data}")
    book = Books.query.filter(Books.id == book_id).first()
    print(book.author)
    # db [author1 ,author2]
    # data [author3]

    del_author = []
    for _author in book.author:
        if _author.name in data['author']:
            data['author'].remove(_author.name)
        else:
            del_author.append(_author)

    for _del_author in del_author:
        book.author.remove(_del_author)

    if data['author']:
        for _author in data['author']:
            book.author.append(Author(name=_author))

    del_publish = []
    for _publish in book.publisher:
        if _publish.name in data['publisher']:
            data['author'].remove(_publish.name)
        else:
            del_publish.append(_publish)
    for _del_publish in del_publish:
        book.author.remove(_del_publish)
    if data['publisher']:
        for _publish in data['author']:
            book.publisher.append(Publish(name=_publish))

    if book.name != data['name']:
        book.name = data['name']

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        data['code'] = 1001
        data['message'] = _("数据保存失败,err=%s") % e

    return data


@api.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Books.query.filter(Books.id == book_id).update({"is_delete": True})
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        data['code'] = 1001
        data['message'] = _("数据保存失败,err=%s") % e
    return data
