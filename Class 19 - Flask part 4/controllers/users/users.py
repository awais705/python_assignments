from flask import Blueprint,request
from services import token_services
from validations.users import validate_user_data,validate_login_data
from models.users.users import add_new_customer,get_role_id, add_user_role,check_login_details


users_bp = Blueprint("usersbp",__name__)


@users_bp.route("/")
def index():
    return "Welcome to Library Management System"


@users_bp.route('/register',methods=["POST"])
def register_user():
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
    
    data = request.get_json()
    if (error := validate_user_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    
    user_id = add_new_customer(name, email, password)
   
    if user_id is not None:
        role_id = get_role_id(role)
        if role_id : 
            user_role_id = add_user_role(user_id,role_id)
            if user_role_id  is not None:
                   return {
                        "data": {"id": user_id}
                    }, 200
    return {
        "data": {"id": user_id}
    }, 200


@users_bp.route('/login',methods=["POST"])
def login_user():
    if not request.is_json:
        return {
            "error": {
                "message": "API accepts json data"
            }
        }, 400
    data = request.get_json()
    if (error := validate_login_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    user_id = check_login_details(email,password,role)
   
    if (user_id != None):
        return {
            "message": "user login successfully",
            "token": token_services.enrypt(user_id["id"])
        }, 200
    else:
        return {
            "error": {
                "message": "invalid email or password"
            }
        }, 400

 
