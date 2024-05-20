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
from http.client import HTTPException

from app.extensions import db
from app.models.book import Author
from app.schemas.authors import AuthorSchema


class AuthorDao(object):

    @staticmethod
    def list_author(offset=0, limit=10):
        return Author.query.filter_by(is_deleted=False).offset(offset).limit(limit).all()

    @staticmethod
    def get_author_by_id(id):
        return Author.query.filter_by(id=id, is_deleted=False).first()

    @staticmethod
    def get_author_by_name(name):
        return Author.query.filter_by(name=name, is_deleted=False).first()

    @staticmethod
    def create_author(authors):
        if not isinstance(authors, list):
            authors = [authors]
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
        return _authors

    @staticmethod
    def delete_author(ids):
        try:
            for id in ids:
                author = Author.query.filter_by(id=id).first()
                if author:
                    author.is_deleted = 1
                    book.deleted_at = datetime.now()
        except Exception as e:
            db.session.rollback()
            raise e
        db.session.commit()

    @staticmethod
    def edit_author(id, data):
        author = Author.query.filter_by(id=id, is_deleted=False).first()
        if not author:
            raise HTTPException(status_code=404, detail='Author not found')

        # 将新的数据加载到现有的author对象实例中
        # schema = AuthorSchema()
        # schema.load(data, instance=author, session=db.session)
        # 更新作者对象的字段
        for key, value in data.items():
            setattr(author, key, value)
        db.session.add(author)
        db.session.commit()
        # 保存更新到数据库
        # return updated_author
