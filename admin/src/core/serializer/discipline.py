from marshmallow import Schema, fields


class DisciplineSchema(Schema):
    name = fields.Str()
    nameInstructors = fields.Str()
    daysAndHours = fields.Str()
    monthlyCost = fields.Int()