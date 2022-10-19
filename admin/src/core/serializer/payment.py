from marshmallow import Schema, fields

class PaymentSchema(Schema):
    total = fields.Int()
    date = fields.Date()