from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from src.core.payment.payment import Mes

class PaymentInfoSchema(Schema):
    mes = EnumField(Mes)
    total = fields.Int()
    nroComprobante = fields.Int()
    