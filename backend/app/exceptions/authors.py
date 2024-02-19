#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/19 15:30                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>
from flask_babel import _
from app import exceptions


class AuthorNotFound(exceptions.NotFound):
    code = 3001
    message = _("Author %(author_id)s not found.")


class AuthorAlreadyExists(exceptions.ExistsError):
    code = 3002
    message = _("Author %(author_id)s already exists.")


class AuthorCreationError(exceptions.CreateError):
    code = 3003
    message = _("Author %(author_id)s create failed")


class AuthorDeletionError(exceptions.DeleteError):
    code = 3004
    message = _("Author %(author_id)s delete failed")

