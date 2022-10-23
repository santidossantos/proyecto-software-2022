from src.core.database import db
from src.core.disciplines.discipline import Discipline
from src.core.associates.associate import associates_disciplines

def find_inscription_by_associate_and_discipline(idAssociate, idDiscipline):
    return (
        db.session.query(associates_disciplines)
        .filter_by(associate_id=idAssociate, discipline_id=idDiscipline)
        .first()
    )