#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

from flask_babel import lazy_gettext as _


class AppException(Exception):
    msg = _("Internal Server Error")
    http_code = 500

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs
        if not message:
            try:
                message = self.message % kwargs
            except Exception as e:
                # LOG.exception(_('Exception in string format operation'))
                for name, value in kwargs.iteritems():
                    # LOG.error("%s: %s" % (name, value))
                    pass
                # at least get the core message out if something happened
                message = self.message
        self.message = message

        super(AppException, self).__init__(message)


class DBException(AppException):
    http_code = 200

    def __init__(self, message=None):
        self.message = 'Failed to connect to database: {}'.format(message)


class NotFound(AppException):
    http_code = 404
    message = _("Resource not be Found")


class ExistsException(AppException):
    http_code = 409
    message = _("Failed to add author %(author_name)s")


class AuthorCreateException(AppException):
    http_code = 500
    message = _("Failed to create author %(author_name)s")


class AuthorUpdateException(AppException):
    http_code = 500
    message = _("Failed to update author %(author_name)s")


class AuthorDeleteException(AppException):
    http_code = 500
    message = _("Failed to delete author %(author_name)s")


class BookCreateException(AppException):
    http_code = 500
    message = _("Failed to create book %(book_name)s")


class BookUpdateException(AppException):
    http_code = 500
    message = _("Failed to update book %(book_name)s")


class BookDeleteException(AppException):
    http_code = 500
    message = _("Failed to delete book %(book_name)s")
