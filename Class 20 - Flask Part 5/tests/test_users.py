from typing import Any
import pytest
import sys
import random
import string
sys.path.append(".")  # Adds higher directory to python modules path.

from models.users.add_new_user import add_new_user



from main import app
from db import mysqlconnect, disconnect


from services import token_services

def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


@pytest.fixture()
def add_db_dump():
   
    # create new user
    name = "TEST SUPER ADMIN"
    email = random_char(5)+"@gmail.com"
    password =  "1234567"
    role = "SUPER_ADMIN"

    user_id = add_new_user(name,email,password,role)

    # new user ID
    return {
      "user_id": user_id,
      "access_token": token_services.encrypt(user_id,"SUPER_ADMIN")
    }


def test_add_user_api_happy_case(add_db_dump: dict[str, Any]):
    print("new user data", add_db_dump)
    access_token = add_db_dump['access_token']
    
    response = app.test_client().post("/add_user", json={
    "name":"TEST ADMIN",
    "email": "random_char(5)+@gmail.com",
    "password": "1234567",
    "role":"ADMIN"
}, headers={
        "Authorization": "Bearer " + access_token
    })

    data = response.json
    assert type(data) is dict
    assert data['data']['id'] > 0


def test_add_user_api_unhappy_case_without_password(add_db_dump: dict[str, Any]):
    print("new user data", add_db_dump)
    access_token = add_db_dump['access_token']
    
    response = app.test_client().post("/add_user", json={
    "name":"TEST ADMIN",
    "email": random_char(5)+"@gmail.com",
    "role":"ADMIN"
}, headers={
        "Authorization": "Bearer " + access_token
    })

    data = response.json
    assert type(data) is dict
    assert data['error']['message'] is not None
    assert data['error']['message'] == "password field is required"

    # assert data is not None
    # assert type(data) is dict
    # assert data['data'] is not None
    # assert data['data']['id']  > 0



def test_user_login_as_super_admin():
    response = app.test_client().post("/login", json={
    "email":"awais705@gmail.com",
    "password": "1234567",
    "role":"SUPER_ADMIN"
})

    data = response.json
    assert type(data) is dict
    assert data["message"] is not None
    assert data['message'] == "user login successfully"
    assert data['token'] is not None 


def test_user_login_as_admin():
    response = app.test_client().post("/login", json={
    "email":"awais705@gmail.com",
    "password": "1234567",
    "role":"ADMIN"
})

    data = response.json
    assert type(data) is dict
    assert data["message"] is not None
    assert data['message'] == "user login successfully"
    assert data['token'] is not None 


def test_user_login_as_staff():
    response = app.test_client().post("/login", json={
    "email":"awais705@gmail.com",
    "password": "1234567",
    "role":"STAFF"
})

    data = response.json
    assert type(data) is dict
    assert data["message"] is not None
    assert data['message'] == "user login successfully"
    assert data['token'] is not None 


def test_user_login_unhappy_case_without_password():
    response = app.test_client().post("/login", json={
    "email":"awais705@gmail.com",
    "role":"SUPER_ADMIN"
})

    data = response.json
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]['message'] == "password field is required"


def test_user_login_unhappy_case_without_wrong_login():
    response = app.test_client().post("/login", json={
    "email":"awais705@gmail.com",
    "password": "1234567d",
    "role":"SUPER_ADMIN"
})

    data = response.json
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]['message'] is not None
    assert data["error"]['message'] == "invalid email or password"



def update_user_api_happy_case(add_db_dump):
    print("new user data", add_db_dump)
    access_token = add_db_dump['access_token']
    
    response = app.test_client().put("/update_user", json={
    "name":"Nazim Hussain",
    "email":"tedijo705@hotmail.com",
    "id":"4"
}, headers={
        "Authorization": "Bearer " + access_token
    })

    data = response.json
    assert type(data) is dict
    assert data['data']['message'] is not None
    assert data['data']['message'] == "Data Updated"


def update_user_api_unhappy_case_with_wrong_id(add_db_dump):
    print("new user data", add_db_dump)
    access_token = add_db_dump['access_token']
    
    response = app.test_client().put("/update_user", json={
    "name":"Nazim Hussain",
    "email":"tedijo705@hotmail.com",
    "id":"4000"
}, headers={
        "Authorization": "Bearer " + access_token
    })

    data = response.json
    assert type(data) is dict
    assert data['error']['message'] is not None
    assert data['error']['message'] == "Invalid Data"



def update_delete_user_happy_case(add_db_dump):
    print("new user data", add_db_dump)
    access_token = add_db_dump['access_token']
    
    response = app.test_client().delete("/delete_user", json={
    "id":"4"
}, headers={
        "Authorization": "Bearer " + access_token
    })

    data = response.json
    assert type(data) is dict
    assert data['data']['message'] is not None
    assert data['data']['message'] == "Data Updated"







    

