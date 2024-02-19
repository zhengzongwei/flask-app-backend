#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/2/5 16:14                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from flask_babel import _
from app.common.utils.logs import Logger

logger = Logger("exceptions")


class BaseException(Exception):
    code = 0
    message = _("An unknown exception occurred.")

    def __init__(self, **kwargs):
        try:
            super().__init__(self.message % kwargs)
            self.msg = self.message % kwargs
            # self.code = self.code

            logger.error(self.msg, 4)
        except Exception:
            pass
            # with excutils.save_and_reraise_exception() as ctxt:
            #     if not self.use_fatal_exceptions():
            #         ctxt.reraise = False
            #         # at least get the core message out if something happened
            #         super().__init__(self.message)
        # super().__init__(self.message % kwargs)
        # self.msg = self.message % kwargs

    def __str__(self):
        # return {"msg": self.msg, "code": self.code}
        return self.msg


class NotFound(BaseException):
    pass


class ExistsError(BaseException):
    pass


class CreateError(BaseException):
    pass


class DeleteError(BaseException):
    pass
