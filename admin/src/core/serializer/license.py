from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from src.core.associates.associate import DocumentType
from src.core.associates.associate import Genero


class LicenseSchema(Schema):
    """A class to represent the JSON format in which an user license will be exported"""
    name = fields.Str()
    last_name = fields.Str()
    dni = fields.Str()
    email = fields.Str()
    mobile_number = fields.Str()
    document_type = EnumField(DocumentType)
    member_number = fields.Str()
    genero = EnumField(Genero)
    address = fields.Str()
    status = fields.Str()
    profile_picture = fields.Str()
    id = fields.Int()
    defaulter = fields.Bool()
    create_at = fields.Date('%d/%m/%Y')
