from src.core.permissions import role
from src.core import auth
from src.core import associates
from src.core import disciplines
from src.core import auth
from src.core import config
from src.core import permissions


def run():
    """Creates all models and tables in the database and fill tables with 
    testing data"""

    config.create()

    user_index = permissions.create_permission(nombre="user_index")
    user_new = permissions.create_permission(nombre="user_new")
    user_destroy = permissions.create_permission(nombre="user_destroy")
    user_update = permissions.create_permission(nombre="user_update")
    user_show = permissions.create_permission(nombre="user_show")
    user_activ = permissions.create_permission(nombre="user_activ")

    member_index = permissions.create_permission(nombre="member_index")
    member_new = permissions.create_permission(nombre="member_new")
    member_destroy = permissions.create_permission(nombre="member_destroy")
    member_update = permissions.create_permission(nombre="member_update")
    member_show = permissions.create_permission(nombre="member_show")

    discipline_index = permissions.create_permission(nombre="discipline_index")
    discipline_new = permissions.create_permission(nombre="discipline_new")
    discipline_destroy = permissions.create_permission(nombre="discipline_destroy")
    discipline_update = permissions.create_permission(nombre="discipline_update")
    discipline_show = permissions.create_permission(nombre="discipline_show")

    config_index = permissions.create_permission(nombre="config_index")
    config_update = permissions.create_permission(nombre="config_update")

    payment_index = permissions.create_permission(nombre="payment_index")
    payment_show = permissions.create_permission(nombre="payment_show")
    payment_create = permissions.create_permission(nombre="payment_create")
    payment_update = permissions.create_permission(nombre="payment_update")

    inscription_index = permissions.create_permission(nombre="inscription_index")
    inscription_create = permissions.create_permission(nombre="inscription_create")

    role_admin = permissions.create_role(nombre="admin")

    role_admin.permisos.append(user_index)
    role_admin.permisos.append(user_new)
    role_admin.permisos.append(user_destroy)
    role_admin.permisos.append(user_update)
    role_admin.permisos.append(user_show)
    role_admin.permisos.append(user_activ)

    role_admin.permisos.append(member_index)
    role_admin.permisos.append(member_new)
    role_admin.permisos.append(member_destroy)
    role_admin.permisos.append(member_update)
    role_admin.permisos.append(member_show)

    role_admin.permisos.append(discipline_index)
    role_admin.permisos.append(discipline_new)
    role_admin.permisos.append(discipline_destroy)
    role_admin.permisos.append(discipline_update)
    role_admin.permisos.append(discipline_show)

    role_admin.permisos.append(config_index)
    role_admin.permisos.append(config_update)

    role_admin.permisos.append(payment_index)
    role_admin.permisos.append(payment_show)
    role_admin.permisos.append(payment_create)
    role_admin.permisos.append(payment_update)

    role_admin.permisos.append(inscription_index)
    role_admin.permisos.append(inscription_create)

    role_operator = permissions.create_role(nombre="operator")

    role_operator.permisos.append(user_index)

    role_operator.permisos.append(member_index)
    role_operator.permisos.append(member_new)
    role_operator.permisos.append(member_update)
    role_operator.permisos.append(member_show)

    role_operator.permisos.append(discipline_index)
    role_operator.permisos.append(discipline_new)
    role_operator.permisos.append(discipline_update)
    role_operator.permisos.append(discipline_show)

    role_operator.permisos.append(inscription_index)
    role_operator.permisos.append(inscription_create)

    rol_associado = permissions.create_role(nombre="associated")

    user_admin = auth.create_user(
        name="Admin",
        last_name="Admin",
        email="admin@gmail.com",
        password="1234",
        user_name="admin_user",
    )
    auth.update_roles(user_admin, [role_admin])

    user_operador = auth.create_user(
        name="Operador",
        last_name="Apellido",
        email="operador@gmail.com",
        password="1234",
        user_name="operator_user",
    )

    auth.update_roles(user_operador, [role_operator])

    associates.create_user(
        name="Lore",
        last_name="Othaz",
        dni="11234599",
        address="City Bell 1500",
        email="lorena@gmail.com",
        mobile_number="2216663811",
    )

    associates.create_user(
        name="Juan",
        last_name="Perez",
        dni="74562198",
        address="6 y 62",
        email="juan@gmail.com",
        mobile_number="2213333838",
    )

    associates.create_user(
        name="Pedro",
        last_name="Picapiedra",
        dni="73456018",
        address="511 y 10",
        email="pedrito@gmail.com",
        mobile_number="2215263838",
    )

    associates.create_user(
        name="Martin",
        last_name="Rodriguez",
        dni="3456099",
        address="Saladillo BSAS.",
        email="martin@outlook.com",
        mobile_number="2216663838",
    )

    disciplines.create_discipline(
        name="Fútbol",
        category="Primera",
        nameInstructors="Gonza , Juana",
        daysAndHours="Lunes a Viernes 10AM",
        monthlyCost=6000,
    )

    disciplines.create_discipline(
        name="Tenis",
        category="ATP",
        nameInstructors="Sofi , Cata",
        daysAndHours="Jueves 15PM",
        monthlyCost=8000,
    )

    disciplines.create_discipline(
        name="Basket",
        category="NBA",
        nameInstructors="Luna",
        daysAndHours="Martes 18HS, Jueves 14HS",
        monthlyCost=3000,
    )

    print("Seeds cargados!")
