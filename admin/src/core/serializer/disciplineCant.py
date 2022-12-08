from marshmallow import Schema, fields


class DisciplineCantSchema(Schema):
    """A class to represent the JSON format in which a discipline and their enrolees
     will be exported"""
    disciplina = fields.Str()
    inscriptos = fields.Str()