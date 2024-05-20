#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.
from app.extensions import db
from app.models.book import Author
from app.schemas.authors import AuthorSchema


class AuthorDao(object):

    @staticmethod
    def list_author():
        return Author.query.filter_by(is_deleted=False).all()

    @staticmethod
    def get_author_by_id(id):
        return Author.query.filter_by(id=id, is_deleted=False).first()

    @staticmethod
    def get_author_by_name(name):
        return Author.query.filter_by(name=name, is_deleted=False).first()

    @staticmethod
    def create_author(authors):
        schema = AuthorSchema()
        _authors = []
        for author in authors:
            existing_author = Author.query.filter_by(name=author.name).first()
            if existing_author:
                _authors.append(existing_author)
            else:
                author_dict = schema.dump(author)
                author = Author(**author_dict)
                db.session.add(author)

                _authors.append(author)

        db.session.add_all(_authors)
        db.session.commit()
