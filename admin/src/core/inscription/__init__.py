from src.core.associates.associate import Associate
from src.core.disciplines.discipline import Discipline
from src.core.disciplines.discipline import UserDiscipline

from src.core.database import db

def createInscription(idAsociado,idDisciplina):
    UserDiscipline = UserDiscipline(user_id=idAsociado, discipline_id=idDisciplina)
    db.session.add(UserDiscipline)
    db.session.commit()
    return UserDiscipline