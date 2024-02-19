#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/19 15:30                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask_babel import _
from app import exceptions


class BookNotFound(exceptions.NotFound):
    code = 4001
    message = _("Book %(book_id)s not found.")


class BookAlreadyExists(exceptions.ExistsError):
    code = 4002
    message = _("Book %(book_name)s already exists.")


class BookCreationError(exceptions.CreateError):
    code = 4003
    message = _("Book %(book_name)s create failed")


class BookDeletionError(exceptions.DeleteError):
    code = 4004
    message = _("Book %(book_name)s delete failed")
