from src.core.permissions import role
from src.core import auth
from src.core import associates
from src.core import disciplines
from src.core import auth
from src.core import payment
from src.core import config
from src.core import permissions


def run():

    config.create()

    permissions.create_permission(nombre="member_index")
    permissions.create_permission(nombre="member_new")
    permissions.create_permission(nombre="member_destroy")
    permissions.create_permission(nombre="member_update")
    permissions.create_permission(nombre="member_show")

    permissions.create_permission(nombre="discipline_index")
    permissions.create_permission(nombre="discipline_new")
    permissions.create_permission(nombre="discipline_destroy")
    permissions.create_permission(nombre="discipline_update")
    permissions.create_permission(nombre="discipline_show")

    # FALTA LINKEAR LOS ROLES CON LOS PERMISOS

    role_admin = permissions.create_role(nombre="admin")
    role_operator = permissions.create_role(nombre="operator")
    permissions.create_role(nombre="associated")




    user_admin = auth.create_user(
        name="Admin", last_name="Admin", email="admin@gmail.com", password="1234"
    )
    auth.update_roles(user_admin, [role_admin])

    user_operador = auth.create_user(
        name="Operador",
        last_name="Apellido",
        email="operador@gmail.com",
        password="1234",
    )

    auth.update_roles(user_operador, [role_operator])

    associates.create_user(
        name="Lore",
        last_name="Othaz",
        dni="11234599",
        address="City Bell 1500",
        email="lorena@gmail.com",
        mobile_number='2216663811'
    )

    associates.create_user(
        name="Juan",
        last_name="Perez",
        dni="74562198",
        address="6 y 62",
        email="juan@gmail.com",
        mobile_number='2213333838'
    )

    associates.create_user(
        name="Pedro",
        last_name="Picapiedra",
        dni="73456018",
        address="511 y 10",
        email="pedrito@gmail.com",
        mobile_number='2215263838'
    )

    associates.create_user(
        name="Martin",
        last_name="Rodriguez",
        dni="3456099",
        address="Saladillo BSAS.",
        email="martin@outlook.com",
        mobile_number='2216663838'
    )

    disciplines.create_discipline(
        name="Fútbol",
        category="Primera",
        nameInstructors="Gonza , Juana",
        daysAndHours="Lunes a Viernes 10AM",
        monthlyCost=6000
    )

    disciplines.create_discipline(
        name="Tenis",
        category="ATP",
        nameInstructors="Sofi , Cata",
        daysAndHours="Jueves 15PM",
        monthlyCost=8000
    )


    disciplines.create_discipline(
        name="Basket",
        category="NBA",
        nameInstructors="Luna",
        daysAndHours="Martes 18HS, Jueves 14HS",
        monthlyCost=3000
    )

    

    print("Seeds cargados!")
