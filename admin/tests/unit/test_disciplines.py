from src.core import disciplines
from src.core import associates

def test_create_discipline(app, fixture_disciplines):
    discipline = fixture_disciplines
    assert discipline.name == "Hockey"
    assert discipline.category == "Categoria 1"
    assert discipline.nameInstructors == "Juan, Pedro, Martina"
    assert discipline.daysAndHours == "Lunes 10AM"
    assert discipline.monthlyCost == 3500
    assert discipline.active == True


def test_update_discipline(app, fixture_disciplines):
    discipline = fixture_disciplines
    disciplines.update_discipline(
        discipline.id, 
        "Volley Ball",
        "Categoria 2",
        "Martin",
        "Jueves 3PM",
        6000
    )
    assert discipline.name == "Volley Ball"
    assert discipline.category == "Categoria 2"
    assert discipline.nameInstructors == "Martin"
    assert discipline.daysAndHours == "Jueves 3PM"
    assert discipline.monthlyCost == 6000


def test_change_status(app, fixture_disciplines):
    discipline = fixture_disciplines
    disciplines.setStatus(discipline.id)
    assert discipline.active == False


def test_enroll_associated(app, fixture_disciplines):
    discipline = fixture_disciplines
    associated = associates.create_user(
        name="Sofi",
        last_name="Raciti",
        dni="1122",
        address="6 y 62",
        email="sofi_r@gmail.com",
        mobile_number="2213333838",
    )
    disciplines.createInscription(associated.id, discipline.id)
    assert disciplines.find_inscription_by_associate_and_discipline(associated.id, discipline.id)
    associates.delete_user_physical(associated.id)