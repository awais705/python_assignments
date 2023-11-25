import pytest
import sys
import random
import string

sys.path.append(".")  # Adds higher directory to python modules path.
from main import app
from db import mysqlconnect, disconnect
from models.users.users import add_new_customer
from services import token_services

def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

# @pytest.fixture()
# def add_db_dump():
#     # create new db session
#     conn = mysqlconnect()
#     conn.cursor()

#     # create new user
#     user_id = add_new_customer(conn, {
#       "name": "Muhammad Hamza",
#       "email": random_char(5)+"@gmail.com",
#       "password": "1234"
#     })

#     # disconnect db session
#     disconnect(conn)

#     # new user ID
#     return {
#       "user_id": user_id,
#       "access_token": token_services.enrypt(user_id)
#     }


def test_register_api_happy_case():
    
    response = app.test_client().post('/register', json={
        "name": "Muhammad Sadiq",
        "email": random_char(5)+"@gmail.com",
        "password": "1234654656",
        "role":"ADMIN"
    })

    data = response.json
    print(data)
    assert type(data['data']) is dict
    assert data['data']['id'] > 0

def test_register_api_unhappy_case():
    
    response = app.test_client().post('/register', json={
        "name": "Muhammad Sadiq",
        "email": random_char(5)+"@gmail.com",
        "role":"ADMIN"
    })

    data = response.json
    assert data['error']['message'] == "password field is required"


def test_login_api_happy_case():
    
    response = app.test_client().post('/register', json={
        "email": "JhQuK@gmail.com",
        "password": "1234654656",
        "role":"ADMIN"
    })

    data = response.json
    
    # assert type(data['data']) is dict
    assert len(data) == 1

def test_login_api_unhappy_case():
    
    response = app.test_client().post('/register', json={
        "email": "JhQuK@gmail.com",
        "password": "asfasdfasdf",
        "role":"ADMIN"
    })

    data = response.json
    
    data['error']['message']  == "invalid email or password"



def test_add_book_api_happy_case():
    response = app.test_client().post('/admin/add_book', json={
        "name": "5AM Club by Robin Sharma",
        "description": "This is a club book ... lorum ipsum lorum ipsum",
        "category":"Self Help",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5fQ.RFsjwlzU0GVXb2cKXn1B4qt_nNZhn6vQ9ujjr8hNNOM"
    })

    data = response.json
    
    assert data["id"] > 0


def test_add_book_api_unhappy_case():
    response = app.test_client().post('/admin/add_book', json={
    "name": "5AM Club by Robin Sharma",
    "description": "This is a club book ... lorum ipsum lorum ipsum",
    "category":"Self Help",
    })

    data = response.json
    #token missing
    assert data["error"]["message"]  == "Token Exipred or wrong token"


    #accept borrow request
def test_accept_borrow_req_api_happy_case():
    response = app.test_client().post('/admin/accept', json={
    "borrow_id": "2",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5fQ.RFsjwlzU0GVXb2cKXn1B4qt_nNZhn6vQ9ujjr8hNNOM"
    })

    data = response.json
    #token missing
    assert len(data['data']) > 1

       #accept borrow request
def test_accept_borrow_req_api_happy_case_without_authorization():
    response = app.test_client().post('/admin/accept', json={
    "borrow_id": "3"
    
    })

    data = response.json
    #token missing
    assert data["error"]["message"]  == "Token Exipred or wrong token"



def test_borrow_listing_req_api_happy_case():
    response = app.test_client().post('/admin/borrow_listing', json={
    "type": "PENDING",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5fQ.RFsjwlzU0GVXb2cKXn1B4qt_nNZhn6vQ9ujjr8hNNOM"
    
    })

    data = response.json
    assert len(data["data"]) > 1



def test_get_all_borrow_list_happy_case():
    response = app.test_client().post('/admin/borrow_listing', json={
    "type": "ALL",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5fQ.RFsjwlzU0GVXb2cKXn1B4qt_nNZhn6vQ9ujjr8hNNOM"
    
    })

    data = response.json
    assert len(data["data"]) > 1


def test_borrow_list_unhappy_case_without_authorization():
    response = app.test_client().post('/admin/borrow_listing', json={
    "type": "ALL",
    
    })

    data = response.json
    
    #token missing
    assert len(data["error"]["message"]) > 0


def test_mark_book_returned_happy_case():
    response = app.test_client().post('/admin/mark_return', json={
    "borrow_id": "2",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5fQ.RFsjwlzU0GVXb2cKXn1B4qt_nNZhn6vQ9ujjr8hNNOM"
    
    })

    data = response.json
    assert int(data["rows_updated"]) == 1


def test_mark_book_returned_unhappy_case_without_borrow_item():
    response = app.test_client().post('/admin/mark_return', json={
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5fQ.RFsjwlzU0GVXb2cKXn1B4qt_nNZhn6vQ9ujjr8hNNOM"
    
    })

    data = response.json
    assert data["error"]["message"] == "Borrow Id field is required"


def test_mark_book_returned_unhappy_case_without_authorization():
    response = app.test_client().post('/admin/mark_return', json={
    "borrow_id": "2",
    })

    data = response.json
    assert data["error"]["message"] == "Token Exipred or wrong token"



    # user
def test_user_registration_happy_case():
    response = app.test_client().post('/register', json={
    "name": "Faraz Ahmed",
    "email": random_char(5)+"@gmail.com",
    "password": random_char(8),
    # "role" : "CUSTOMER"
    "role" : "ADMIN"
    })

    data = response.json
    assert data["data"]["id"] > 0


def test_search_books_happy_case():
    response = app.test_client().get('/customer/search', query_string={'q': 'power'})

    data = response.json
    assert len(data['books']) > 0


def test_search_books_unhappy_case_without_search_term():
    response = app.test_client().get('/customer/search', query_string={'q': ''})

    data = response.json
    assert data["error"]["message"] == "name field is required"


def test_book_listing_pagination_happy_case():
    response = app.test_client().get('/customer/book_listing', query_string={'p': 2})

    data = response.json
    assert len(data['books']) > 0

def test_book_listing_pagination_unhappy_case_without_pageid():
    response = app.test_client().get('/customer/search', query_string={})

    data = response.json
    assert data["error"]["message"] == "name field is required"



def test_borrow_book_happy_case():
    response = app.test_client().post('/customer/borrow_book', json={
    "book_id": "10",
    "to_date": "2023-11-11",
    "from_date":"2023-12-11",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5fQ.RFsjwlzU0GVXb2cKXn1B4qt_nNZhn6vQ9ujjr8hNNOM"
    })

    data = response.json
    assert data["data"]["borrow_id"] > 0


def test_borrow_book_unhappy_case_missing_bookid():
    response = app.test_client().post('/customer/borrow_book', json={
    # "book_id": "10",
    "to_date": "2023-11-11",
    "from_date":"2023-12-11",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5fQ.RFsjwlzU0GVXb2cKXn1B4qt_nNZhn6vQ9ujjr8hNNOM"
    })

    data = response.json
    assert data["error"]["message"] == "Book ID field is required"


def test_borrow_book_unhappy_case_without_authorization():
    response = app.test_client().post('/customer/borrow_book', json={
    "book_id": "10",
    "to_date": "2023-11-11",
    "from_date":"2023-12-11",
    # "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5fQ.RFsjwlzU0GVXb2cKXn1B4qt_nNZhn6vQ9ujjr8hNNOM"
    })

    data = response.json
    assert data["error"]["message"] == "Token Exipred or wrong token"



    
