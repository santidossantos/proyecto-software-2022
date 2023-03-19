from src.core import auth
from src.web.helpers.permission import has_role_by_id
from src.core import permissions


def test_create_user(app, fixture_auth):
    user = fixture_auth
    assert user.name == 'Matias'
    assert user.last_name == 'Robles'
    assert user.email == 'matias@gmail.com'
    assert user.active == True
    assert has_role_by_id(user.id ,"admin")
    

def test_check_password(app, fixture_auth):
    user = fixture_auth
    assert user.check_password("1234")


def test_update_roles(app, fixture_auth):
    user = fixture_auth
    role_operator = permissions.get_role_by_name("operator")
    auth.update_roles(user, [role_operator])
    assert has_role_by_id(user.id , "operator") == True
    

def test_update_user(app, fixture_auth):
    user = fixture_auth
    auth.update_user(id=user.id, name="Pedro", email="pedro@gmail.com", user_name="pedro", password='12345')
    assert user.name == "Pedro"
    assert user.email == "pedro@gmail.com"
    assert user.user_name == "pedro"
    assert user.password == "12345"

    
def test_change_status(app, fixture_auth):
    user = fixture_auth
    auth.setStatus(user.id)
    assert user.active == False

    
