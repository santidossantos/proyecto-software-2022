from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.Str()
    last_name =  fields.Str()
