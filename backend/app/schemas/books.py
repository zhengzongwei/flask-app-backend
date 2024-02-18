#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/6 10:29
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from marshmallow import fields
from marshmallow import validates, ValidationError

from models.book import Book, Author
from flask_babel import _
from app.common.utils.logs import Logger
from app.extensions import ma
from app.schemas.authors import AuthorSchema

logger = Logger("BookSchema")


#
# class PublishSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Publish
#         load_instance = True
#         exclude = ("deleted_at",)


class BookSchema(ma.SQLAlchemyAutoSchema):
    authors = fields.List(fields.Nested(AuthorSchema()))
    isbn = fields.Str(required=True)

    class Meta:
        model = Book
        # 自动加载到实例对象中
        load_instance = True
        include_fk = True
        exclude = ("deleted_at",)

    # authors = fields.List(fields.Nested(AuthorSchema()), required=True)

    # publisher = fields.List(fields.Nested(PublishSchema))

    @validates("authors")
    def validate_authors(self, values):
        if not values:
            raise ValidationError(_("No authors"))

    @validates('name')
    def validate_name(self, value):
        if not value:
            raise ValidationError(_('Name is required.'))

    @validates('publication_date')
    def validate_publication_date(self, value):
        if value.year > 2022:
            raise ValidationError(_('Publication date cannot be in the future'))

    # 删除书籍校验
    @staticmethod
    def validate_delete_book_data(data):
        if not data.get("book_ids"):
            raise ValidationError("Book IDs are required for deletion.")
        if not isinstance(data["book_ids"], list) or not all(isinstance(book_id, int) for book_id in data["book_ids"]):
            raise ValidationError("Invalid book IDs format.")

        return data["book_ids"]


if __name__ == '__main__':
    book_data = [{
        'name': 'Sample Book',
        'authors': [
            {'name': 'john Uh1'},
            {'name': 'john Uh2'},
            {'name': 'john Uh3'},
        ],
        'publication_date': '2021-02-15',
        'isbn': '1234567890'
    }]

    book_schema = BookSchema()
    try:
        # 反序列化数据并进行校验
        book = book_schema.load(book_data, many=True)
        # 如果校验通过，可以将数据保存到数据库中
        # db.session.add(book)
        # db.session.commit()
        print('Book data is valid:', book)
    except ValidationError as err:
        # 校验失败，输出错误信息
        print('Validation error:', err.messages)
