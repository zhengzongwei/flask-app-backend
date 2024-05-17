#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

from datetime import datetime

from app.extensions import db
from app.models.book import Author, Book


class BookDao(object):

    @staticmethod
    def list_book():
        return Book.query.filter_by(is_deleted=False).all()

    @staticmethod
    def create_book(books):
        for book in books:
            authors = []
            for author in book.authors:
                author_name = author.name
                existing_author = Author.query.filter_by(name=author_name).first()
                if existing_author:
                    authors.append(existing_author)
                else:
                    new_author = Author(name=author_name)
                    db.session.add(new_author)
                    authors(new_author)
                book.authors = authors
        db.session.add_all(books)
        db.session.commit()

    @staticmethod
    def delete_book(book_ids):
        try:
            # 检查书籍是否存在
            for book_id in book_ids:
                book = Book.query.filter_by(id=book_id).first()
                if book:
                    book.authors.clear()
                    # db.session.delete(book)
                    book.is_delete = 1
                    book.deleted_at = datetime.now()
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.filter_by(id=book_id, is_deleted=False).first()

    @staticmethod
    def get_book_by_name(name):
        return Book.query.filter_by(name=name, is_deleted=False).first()
