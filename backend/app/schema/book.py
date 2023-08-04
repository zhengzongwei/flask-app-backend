from app.common.common import ma
from marshmallow import fields, validates, ValidationError


class BookSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    common = fields.String()
    author = fields.List(fields.String(required=True))
    publisher = fields.List(fields.String(required=True))

    @validates("name")
    def validate_name(self, value):
        if not value:
            raise ValidationError("name is None")
