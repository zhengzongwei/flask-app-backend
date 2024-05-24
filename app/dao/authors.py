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
from app.models.book import Author

from app.exceptions import exceptions


class AuthorDao(object):

    @staticmethod
    def list_author(offset=0, limit=10):
        return (
            Author.query.filter_by(is_deleted=False).offset(offset).limit(limit).all()
        )

    @staticmethod
    def get_author_by_id(author_id):
        return Author.query.filter_by(id=author_id, is_deleted=False).first()

    @staticmethod
    def get_author_by_name(name):
        return Author.query.filter_by(name=name, is_deleted=False).first()

    def create_author(self, authors):
        if not isinstance(authors, list):
            authors = [authors]
        _authors = []
        print(authors)
        for author in authors:
            existing_author = self.get_author_by_name(author.name)
            if existing_author:
                _authors.append(existing_author)
            else:
                try:
                    db.session.add(author)
                except Exception as e:
                    db.session.rollback()
                    raise e
                _authors.append(author)
        try:
            db.session.add_all(_authors)
        except Exception as e:
            db.session.rollback()
            raise e
        db.session.commit()
        return _authors

    def delete_author(self, ids):

        try:
            for _id in ids:
                author = self.get_author_by_id(_id)
                if author:
                    author.is_deleted = 1
                    author.deleted_at = datetime.now()
        except Exception as e:
            db.session.rollback()
            raise e
        db.session.commit()

    def edit_author(self, author_id, data):
        author = self.get_author_by_id(author_id=author_id)
        if not author:
            raise exceptions.AuthorNotFound(author_id)

        # 更新作者对象的字段
        for key, value in data.items():
            setattr(author, key, value)
        try:
            db.session.add(author)
        except Exception as e:
            db.session.rollback()
            raise e
        db.session.commit()
