from marshmallow import Schema, fields


class UserSchema(Schema):
    """A class to represent the JSON format in which an associated model"""
    name = fields.Str()
    last_name =  fields.Str()
