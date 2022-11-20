from marshmallow import Schema, fields


class DisciplineCantSchema(Schema):
    disciplina = fields.Str()
    inscriptos = fields.Str()