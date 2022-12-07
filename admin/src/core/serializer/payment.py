from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from src.core.payment.payment import Mes

class PaymentSchema(Schema):
    """A class to represent the JSON format in which a Payment model
     will be exported"""
    mes = EnumField(Mes)
    total = fields.Int()
    nroComprobante = fields.Int()