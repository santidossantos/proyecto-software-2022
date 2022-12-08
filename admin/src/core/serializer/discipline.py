from marshmallow import Schema, fields


class DisciplineSchema(Schema):
    """A class to represent the JSON format in which a discipline model will be exported"""
    name = fields.Str()
    nameInstructors = fields.Str()
    daysAndHours = fields.Str()
    monthlyCost = fields.Int()