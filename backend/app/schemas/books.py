#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/6 10:29                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from marshmallow import fields, pre_load
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from marshmallow import validates, ValidationError

from app.models.books.book import Book, Author
from flask_babel import _


class AuthorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        # 自动加载到实例对象中
        load_instance = True
        exclude = ("deleted_at",)

    name = fields.String(required=True)


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        # 自动加载到实例对象中
        load_instance = True
        exclude = ("deleted_at",)

    authors = fields.List(fields.Nested(AuthorSchema))

    # def load(self, data, *, many=None, partial=None, **kwargs):
    #     pass

    @pre_load
    def pre_load(self, data, many=None, **kwargs):
        print(data)
        authors = data.get("authors", [])
        _authors = []
        for author in authors:
            author_name = author.get('name')
            existing_author = Author.query.filter_by(name=author_name).first()

            if not existing_author:
                Author(name=author_name)

                # _authors.append(existing_author)
            # else:

            # _authors.append(new_author)
        # data["authors"] = _authors
        # print(_authors)
        # print(data,'123')
        return data

    # @validates("authors")
    # def validate_authors(self, values):
    #     if not values:
    #         raise ValidationError(_("No authors"))

    @validates('name')
    def validate_name(self, value):
        if not value:
            raise ValidationError(_('Name is required.'))

    @validates('publication_date')
    def validate_publication_date(self, value):
        if value.year > 2022:
            raise ValidationError(_('Publication date cannot be in the future'))


if __name__ == '__main__':
    book_data = {
        'name': 'Sample Book',
        'author': 'John Doe',
        'publication_date': '2021-02-15',
        'isbn': '1234567890'
    }

    book_schema = BookSchema()
    try:
        # 反序列化数据并进行校验
        book = book_schema.load(book_data)
        # 如果校验通过，可以将数据保存到数据库中
        # db.session.add(book)
        # db.session.commit()
        print('Book data is valid:', book)
    except ValidationError as err:
        # 校验失败，输出错误信息
        print('Validation error:', err.messages)
