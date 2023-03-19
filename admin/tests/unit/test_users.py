from src.core import auth
from src.web.helpers.permission import has_role_by_id


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
    auth.update_roles(user, 'operator')
    assert has_role_by_id(user.id ,"operator")
    
