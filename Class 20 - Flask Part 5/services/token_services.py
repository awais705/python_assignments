from flask import Flask,request
import jwt
from functools import wraps
# from main import app

from datetime import timedelta

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


# app = Flask(__name__)



# # https://flask-jwt-extended.readthedocs.io/en/stable/options.html
# app.config["JWT_SECRET_KEY"] = "its-not-over-until-i-win"  # Change this!
# app.config["JWT_TOKEN_LOCATION"] = ["headers"] # specifying the location of JWT 
# app.config["JWT_ALGORITHM"] = "HS256" # symmetric keyed hashing algorithm
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=10)
# app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

# jwt = JWTManager(app)



def superadmin_token_required(func):
    @wraps(func)
    @jwt_required()
    def _token_required(*args, **kwargs):
        
       # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()

        user_info = current_user.split("-")
        login_id = user_info[0]
        login_as = user_info[1]

        if login_as is None or login_as != "SUPER_ADMIN":
            return {
            "error": {"message": "Only Super Admin can perform this action"}
        }, 400
        
        decoded_data  = {'login_id':str(login_id),
                     'user_type': str(login_as)}
        
        response =  func(decoded_data, *args, *kwargs)
        # print("after my_profile")

        return response
    return _token_required



def admin_token_required(func):
    @wraps(func)
    @jwt_required()
    def _admin_token_required(*args, **kwargs):
        
       # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()

        user_info = current_user.split("-")
        login_id = user_info[0]
        login_as = user_info[1]

        if login_as is None or login_as == "STAFF":
            return {
            "error": {"message": "Only Super Admin and admin can perform this action"}
        }, 400
        
        decoded_data  = {'login_id':str(login_id),
                     'user_type': str(login_as)}
        
        response =  func(decoded_data, *args, *kwargs)
        # print("after my_profile")

        return response
    return _admin_token_required



def admin_only_token_required(func):
    @wraps(func)
    @jwt_required()
    def _admin_only_token_required(*args, **kwargs):
        
       # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()

        user_info = current_user.split("-")
        login_id = user_info[0]
        login_as = user_info[1]

        if login_as is None or login_as == "STAFF" or login_as == "SUPER_ADMIN":
            return {
            "error": {"message": "Only Admin can perform this action"}
        }, 400
        
        decoded_data  = {'login_id':str(login_id),
                     'user_type': str(login_as)}
        
        response =  func(decoded_data, *args, *kwargs)
        # print("after my_profile")

        return response
    return _admin_only_token_required





def encrypt(user_id,role):
    identity = str(user_id) +"-" + str(role)
    # token = jwt.encode({"user_id": user_id}, SECRET, algorithm="HS256")
    access_token = create_access_token(identity=identity)
    return access_token



def staff_token_required(func):
    @wraps(func)
    @jwt_required()
    def _staff_token_required(*args, **kwargs):
        
       # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()

        user_info = current_user.split("-")
        login_id = user_info[0]
        login_as = user_info[1]

        if login_as is None or login_as == "ADMIN":
            return {
            "error": {"message": "Only STAFF and SUPER ADMIN can perform this action"}
        }, 400
        
        decoded_data  = {'login_id':str(login_id),
                     'user_type': str(login_as)}
        
        response =  func(decoded_data, *args, *kwargs)
        # print("after my_profile")

        return response
    return _staff_token_required


def staff_only_token_required(func):
    @wraps(func)
    @jwt_required()
    def _staff_only_token_required(*args, **kwargs):
        
       # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()

        user_info = current_user.split("-")
        login_id = user_info[0]
        login_as = user_info[1]

        if login_as is None or login_as == "ADMIN" or login_as == "SUPER_ADMIN":
            return {
            "error": {"message": "Only STAFF can perform this action"}
        }, 400
        
        decoded_data  = {'login_id':str(login_id),
                     'user_type': str(login_as)}
        
        response =  func(decoded_data, *args, *kwargs)
        # print("after my_profile")

        return response
    return _staff_only_token_required

# @jwt_required()
# def decode():
#     # Access the identity of the current user with get_jwt_identity
#     current_user = get_jwt_identity()
#     return {'logged_in_as':current_user}, 200
