from flask import request
# from query import login_user,register_user,user_login,get_notes_by_id,add_user_notes,get_category_notes_by_id,add_notes_category,assign_category_to_notes
import query 
import jwt
# import json
from functools import wraps

secret_key = "ITSNOTOVERUNTILIWIN"

# create decorator named "token_required" and use it on protected apis
def token_required(func):
    @wraps(func)
    def _token_required(*args, **kwargs):
        
        token = request.args.get("token")
        if token is None:
            new_token  = request.get_json()
            token  = new_token.get("token")

        if token is None or len(token) <= 0:
            return {
            "error": {"message": "Token Exipred or wrong token "}
        }, 400

       
        # verify token
        user=jwt.decode(
            token, 
            secret_key, 
            algorithms="HS256"
        )
        # print("user", user)
       
        response =  func(user, *args, *kwargs)
        # print("after my_profile")

        return response
    return _token_required



def login():
    auth = request.get_json()

    # if email and password:
    if (error := is_valid_login_data(auth)) is not None:
        return {
            "error": {"message": error}
        }, 400

    login = query.login_user(auth)
    if login is None:
        # log.warning("employee not found")
        return {
            "error": {"message": "Invalid login details "}
        }, 400

    # return {
    #     "data": login
    # }, 200

    token_data = {
         'username': login['username'],
         'email': login['email'],
         'user_id': login['id']
    }   

    #create token 
    token  = jwt.encode(token_data,secret_key,algorithm="HS256")
    
    #add user login 
    query.user_login(login["id"],token)
    
    return token,200




#Validate login data
def is_valid_login_data(data):
    error_msg = None

    if data.get("password") is None or len(data.get("password").strip()) == 0:
        error_msg = "email field is required"

    if data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"

    return error_msg


# Register user
def register():
    reg = request.get_json()

    if (error := is_validate_register_data(reg)) is not None:
        return {
            "error": {"message": error}
        }, 400

    # register variable will contain inserted id of user
    register = query.register_user(reg)
    if register is None:
        # log.warning("employee not found")
        return {
            "error": {"message": "Registration failed. Please try again later!"}
        }, 400
    
    return {
        "data": register
    }






# Validate register data
def is_validate_register_data(data):
    error_msg = None

    if data.get("username") is None or len(data.get("username").strip()) == 0:
        error_msg = "username field is required"

    if data.get("fullname") is None or len(data.get("fullname").strip()) == 0:
        error_msg = "fullname field is required"

    if data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"

    if data.get("password") is None or len(data.get("password").strip()) == 0:
        error_msg = "password field is required"   

    return error_msg    


#Notes 
@token_required
def notes(user):
    
    # token = request.args.get("token")
    user_id = user["user_id"]
    if request.method == "GET":
        data = get_user_notes(user_id)
    else:
        data = add_notes(user_id)    
    
    return data

#add notes 
def add_notes(user_id):
    
    notes_data = request.get_json()

    if (error := is_validate_notes_data(notes_data)) is not None:
        return {
            "error": {"message": error}
        }, 400
    

    # if notes_data and len(notes_data["token"]).strip() > 0:
    # decode = decode_access_token(notes_data["token"])    

    # if decode and decode["user_id"] > 0:
    notes_data["user_id"] = user_id
    
    # return notes_data
    notes_id = query.add_user_notes(notes_data)
    if notes_id is None:
        # log.warning("employee not found")
        return {
            "error": {"message": " Something happend. Please try again later!"}
        }, 400
    
    if "category" in notes_data:
        query.add_notes_category(notes_id, notes_data["category"],notes_data["user_id"])
        
    
    return {
        "data": notes_id
    }

#retrieve notes
def get_user_notes(user_id):
    # data = decode_access_token(token)
    if user_id is not None:
        # user_id = data.get("user_id")
        notes = query.get_notes_by_id(user_id)

        if notes is None:
        # log.warning("employee not found")
            return {
                "error": {"message": "No record exist"}
            }, 400
    
        return {
            "data": notes
        }
    


# decode access token
def decode_access_token(token):
    # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF3YWlzNzA1IiwiZW1haWwiOiJhd2FpczcwNUBnbWFpbC5jb20ifQ.F5B4wY1M2xwyUXCIfgV7WjUqS57uPAEY6gaGws5covE"
    decoded_token = jwt.decode(
        token,
        secret_key,
        algorithms="HS256"
    )

    return decoded_token


def is_validate_notes_data(data):
    error_msg = None

    if data.get("title") is None or len(data.get("title").strip()) == 0:
        error_msg = "title field is required"


    if data.get("token") is None or len(data.get("token").strip()) == 0:
        error_msg = "token field is required"

        


    return error_msg    

#category notes fetching / assign category to notes
@token_required
def category(user):
    user_id = user["user_id"]
    if request.method == "GET":
        data = get_category_notes(user_id)
    else:
        data = assign_notes_category(user_id)    
    
    return data
    

#category notes based on user id

def get_category_notes(user_id):

    # user_id = user["user_id"]

    #need to send data in json format
    search_data = request.get_json()
    # token  = search_data.get("token")
    
    # data = decode_access_token(token)

     #category need to be an ID
    cat = search_data.get("cat") 
    

    if search_data is None:
        return {
                "error": {"message": "Category info is not valid"}
            }, 400

    
    if user_id is not None and cat:
        
        notes = query.get_category_notes_by_id(user_id,cat)

        if notes is None:
        # log.warning("employee not found")
            return {
                "error": {"message": "No record exist"}
            }, 400
    
        return {
            "data": notes
        }
    else:
         return {
                "error": {"message": "Search filters are missing"}
            }, 400
    


def assign_notes_category(user_id): 
   #need to send data in json format
    data = request.get_json()
    # token  = data.get("token")
    
    # token_data = decode_access_token(token)

     #category need to be an ID
    cat = data.get("cat") 
    note_id = data.get("note_id") 
    # user_id = user["user_id"]
    

    if user_id is None:
        return {
                "error": {"message": "Login required to assign category to notes"}
            }, 400
    
    if cat is None or note_id is None:
        return {
                "error": {"message": "Details are not correct. Please check again"}
            }, 400
    

    assign = query.assign_category_to_notes(cat,note_id,user_id)

    if assign is None:
        # log.warning("employee not found")
            return {
                "error": {"message": "Failed to Add category"}
            }, 400
    
    return {
    "data": assign
    }
  


