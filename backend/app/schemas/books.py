#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/6 10:29                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from marshmallow import validates, ValidationError

from app.models.books.book import Book
from flask_babel import _


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        # 自动加载到实例对象中
        load_instance = True

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
