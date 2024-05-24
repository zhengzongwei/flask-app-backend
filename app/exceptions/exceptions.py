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

    def __init__(self, message, http_code=None, payload=None):
        super().__init__()
        self.message = message
        if http_code is not None:
            self.http_code = http_code
        self.payload = payload


class DBException(AppException):
    http_code = 200

    def __init__(self, message=None):
        self.message = 'Failed to connect to database: {}'.format(message)


class NotFound(AppException):
    msg = _("Resource not be Found")
    http_code = 404


class AuthorNotFound(NotFound):
    msg = _("Author %(author_id)s not be Found")


class BookNotFound(NotFound):
    msg = _("Book %(book_id)s not be Found")
