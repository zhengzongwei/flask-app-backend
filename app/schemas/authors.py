#  Copyright (c)2024. zhengzongwei
#  flask-app-backend is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

from app.models.book import Author
from flask_babel import _
from app.common.utils.logs import Logger
from app.extensions import ma
from marshmallow import validates, ValidationError
from marshmallow import fields

logger = Logger("AuthorSchema")


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    name = fields.String(required=True)
    class Meta:
        model = Author
        # include_fk = True
        # load_instance = True
        exclude = ("deleted_at","is_deleted","created_at","updated_at")

    @validates('name')
    def validate_name(self, name):
        if not name:
            raise ValidationError(_('Name is required.'))



if __name__ == '__main__':
    author = AuthorSchema()
    # author_data = {
    #     "name": "NIEANTAI1",
    #     "phone": "saass",
    #     "addr": "test",
    # }
    # _author = author.load(author_data)
    # print(_author)
