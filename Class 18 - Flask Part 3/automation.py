import random
import string
import requests
import json


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

#login user 
def login_user():
    url = "http://localhost:3000/login"

    r = requests.get(url, json={
    "email": "awais705@gmail.com",
    "password": "123456"
    }
  )
    response_data = r.json()
    print(response_data)
    return response_data


def register_user():
    url = "http://localhost:3000/register"

    r = requests.post(url, json={
        "email" : "hello@cheeltech.com",
        "password" : "WeekendClass19",
        "fullname" : "Muhammad Awais",
        "username" : "Awais bin Sadiq"
        }
    )
    response_data = r.json()
    print(response_data)
    return response_data['data']['id']

#get notes
def get_notes(user_id):
    url = "http://localhost:3000/notes"+ "/"+ str(user_id)
    r = requests.get(url)
    response_data = r.json()
    print(response_data)


def add_notes(user_id):
    url = "http://localhost:3000/notes"

    r = requests.post(url, json={
        "title": "Sunday dawat",
        "category": "Qorma,biryani,Karhai",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF3YWlzNzA1IiwiZW1haWwiOiJhd2FpczcwNUBnbWFpbC5jb20iLCJ1c2VyX2lkIjoxfQ.5LpNhW6rKVMS834B3P5aN3S_Rjg5mFIFidZevQ-EL2M"

        }
    )
    response_data = r.json()
    print(response_data)
    return response_data['data']['id']


def category_notes():
    url = "http://localhost:3000/category"
    r = requests.get(url,json={
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF3YWlzNzA1IiwiZW1haWwiOiJhd2FpczcwNUBnbWFpbC5jb20iLCJ1c2VyX2lkIjoxfQ.5LpNhW6rKVMS834B3P5aN3S_Rjg5mFIFidZevQ-EL2M",
        "cat": "1"
    })
    response_data = r.json()
    print(response_data)



def assign_cat_notes():
    url = "http://localhost:3000/category"

    r = requests.post(url, json={
        
        "cat": "5",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF3YWlzNzA1IiwiZW1haWwiOiJhd2FpczcwNUBnbWFpbC5jb20iLCJ1c2VyX2lkIjoxfQ.5LpNhW6rKVMS834B3P5aN3S_Rjg5mFIFidZevQ-EL2M",
        "note_id" :   "5"  
        }
    )

    response_data = r.json()
    print(response_data)
    return response_data


# check_user_login = login_user()
# print(check_user_login)

# register = register_user()
# print(register)

# notes = get_notes(1)
# print(notes)

# add_note = add_notes(2)
# print(add_note)


# cat_notes = category_notes()
# print(cat_notes)

assign_cat = assign_cat_notes()
print(assign_cat)


