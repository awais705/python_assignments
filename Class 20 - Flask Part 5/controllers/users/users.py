from flask import Blueprint,request
from datetime import date,datetime
from models.users.get_complaint_counts import get_complaint_counts
from validations.users import validate_user_data,validate_login_data,validate_data_for_update
from models.users.add_new_user import add_new_user
from models.users.check_login_details import check_login_details
from models.users.update_user_details import update_user_details
from models.users.soft_delete_user import soft_delete_user
from services.token_services import superadmin_token_required,encrypt

users_bp = Blueprint("usersbp",__name__)



@users_bp.route('/add_user',methods=["POST"])
@superadmin_token_required
def register_user(token_info):
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
    created_by = token_info["login_id"]

    
    user_id = add_new_user(name, email, password,role,created_by)
   
    if user_id is not None:
        return {
            "data": {"id": user_id}
        }, 200

    else:
        return {
            "error": {"message": "Invalid Data"}
        }, 400


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

    user = check_login_details(email,password,role)
   
    if (user != None):
        return {
            "message": "user login successfully",
            "token": encrypt(user['id'],role)
        }, 200
    else:
        return {
            "error": {
                "message": "invalid email or password"
            }
        }, 400
    

@users_bp.route('/update_user',methods=["PUT"])
@superadmin_token_required
def update_user(token_info):
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
    
    data = request.get_json()
    if (error := validate_data_for_update(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    id = data.get("id")
    name = data.get("name",None)
    email = data.get("email",None)
    password = data.get("password",None)


    
    row_updated = update_user_details(id,name, email,password)
   
    if row_updated is not None and row_updated > 0:
        return {
            "data": {"message": "Data Updated"}
        }, 200

    else:
        return {
            "error": {"message": "Invalid Data"}
        }, 400



@users_bp.route('/delete_user',methods=["DELETE"])
@superadmin_token_required
def delete_user(token_info):
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
    
    data = request.get_json()
    if (error := validate_data_for_update(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    id = data.get("id")
    
    row_updated = soft_delete_user(id)
   
    if row_updated is not None:
        return {
            "data": {"message": "User Deleted"}
        }, 200

    else:
        return {
            "error": {"message": "Invalid Data"}
        }, 400


@users_bp.route('/dashboard_stats',methods=["GET"])
@superadmin_token_required
def dashboard_stats(token_info):

    stats = {
        "today_total_complaints_count":{
            "total_complaint_registered": get_complaint_counts("today"),
            "total_resolved_complaints": get_complaint_counts("today", "RESOLVED"),
        },
        "last_7_days_compltains_count" : {
            "total_complaint_registered":get_complaint_counts("weekago"),
            "total_resolved_complaints": get_complaint_counts("weekago", "RESOLVED")
        },
        "last_30_days_compltians_count" : {
            "total_complaint_registered":get_complaint_counts("monthago"),
            "total_resolved_complaints": get_complaint_counts("monthago", "RESOLVED")
        }


    }
   
    if stats is not None:
        return {
            "data": {"data" : stats}
        }, 200

    else:
        return {
            "error": {"message": "Invalid Data"}
        }, 400



@users_bp.route('/test',methods=["GET"])
def testing():
    
    count =  get_complaint_counts("today", "RESOLVED")
    return count




 
