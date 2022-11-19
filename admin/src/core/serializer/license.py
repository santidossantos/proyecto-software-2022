from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from src.core.associates.associate import DocumentType
from src.core.associates.associate import Genero


class LicenseSchema(Schema):
    name = fields.Str()
    last_name = fields.Str()
    dni = fields.Str()
    email = fields.Str()
    mobile_number = fields.Str()
    document_type = EnumField(DocumentType)
    member_number = fields.Str()
    genero = EnumField(Genero)
    address = fields.Str()
    status = fields.Str()  # FALTA DETERMINAR MOROSIDAD
    profile_picture = fields.Str()  # URL de la FOTO no el Binario
