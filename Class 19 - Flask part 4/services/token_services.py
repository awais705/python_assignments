from flask import request
import jwt
from functools import wraps



SECRET = "ITSNOTOVERUNTILIWIN"


# def token_decrypt(func):
#     def _token_decrypt(*args, **kwargs):
#         decoded_data = None
#         try:
#             token = request.args.get("token")
#             if token is None: raise Exception
#             decoded_data = jwt.decode(token, SECRET, algorithms="HS256")
#         except:
#             return {"error": {"message": "Unauthenticated user"}}
#         print(decoded_data)
#         return func(decoded_data["id"], *args, **kwargs)
#     _token_decrypt.__name__ = func.__name__
#     return _token_decrypt


def token_required(func):
    @wraps(func)
    def _token_required(*args, **kwargs):
        
        token = request.args.get("token")
        if token is None:
            new_token  = request.get_json()
            token  = new_token.get("token")

        if token is None or len(token) <= 0:
            return {
            "error": {"message": "Token Exipred or wrong token"}
        }, 400

       
        # verify token
        decode_data=jwt.decode(
            token, 
            SECRET, 
            algorithms="HS256"
        )
    #    print("user", user)
       
        response =  func(decode_data, *args, *kwargs)
        # print("after my_profile")

        return response
    return _token_required


def enrypt(user_id):
    token = jwt.encode({"user_id": user_id}, SECRET, algorithm="HS256")
    return token
