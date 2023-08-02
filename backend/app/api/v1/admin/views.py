from flask import jsonify,request

from . import admin as api

from app.models.book import Books,Author
from app.common.db import db
"""
给接口添加 访问权限，判断是否有权限访问
"""


@api.route('/', methods=['GET', 'POST'])
def books():
    """
    获取所有的书籍
    """
    data = {"code": 0, "message": 'success', 'data': []}
    # get books info from db
    if request.method == "GET":
        books_info = Books.query.all()
        if books:
            print(books)
            for book in books_info:
                data['data'].append(book.to_json())
    elif request.method == "POST":
        request_data = request.get_json()
        # 校验参数
        if 'books' in request_data:
            for book_info in request_data['books']:
                if book_info['name'] and book_info['author']:
                    # author = Books.query.filter(Books.author == book_info['author'])
                    book = Books()
                    author = Author()
                    author_info = author.query.filter(author.name==book_info['author']).first()
                    if not author_info:
                        author.name = book_info['author']

                    book.name = book_info['name']
                    book.author = [author]
                    try:
                        db.session.add_all([book])
                        db.session.commit()
                    except Exception as e:
                        db.session.rollback()
                        # current_app.logger.error(e)
                        data['code'] = 1001
                        data['message'] = "数据保存失败,err=%s" % e
    return data
