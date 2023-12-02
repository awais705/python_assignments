from flask import Blueprint,request
from datetime import date,datetime
from models.admin.assign_complaint_to_staff import assign_complaint_to_staff
from models.admin.mark_complaint_resolved import mark_complaint_resolved
from models.admin.staff_status import staff_status
from models.admin.update_complaint import update_complaint
from services.token_services import admin_token_required,admin_only_token_required
from validations.admins import validate_complain_type_data, validate_complaint_data,validate_update_complaint_data,validate_assign_complaint_data,validate_mark_complaint_data
from models.admin.add_category_type import add_category_type
from models.admin.add_new_complaint import add_new_complaint

admin_bp = Blueprint("adminbp",__name__)


@admin_bp.route('/add_compliant_type',methods=["POST"])
@admin_token_required
def add_compliant_type(token_info):
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
    
    data = request.get_json()

    if (error := validate_complain_type_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    name = data.get("name",None)
    description = data.get("description",None)
    created_by = token_info["login_id"]

    cat_type_id = add_category_type(name, description,created_by)

    if cat_type_id is not None:
        return {
            "data": {"id": cat_type_id}
        }, 200

    else:
        return {
            "error": {"message": "Invalid Data"}
        }, 400


    
@admin_bp.route('/add_compliant',methods=["POST"])
@admin_only_token_required
def add_compliant(token_info):
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
    
    data = request.get_json()

    if (error := validate_complaint_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    title = data.get("title",None)
    description = data.get("description",None)
    created_by = token_info["login_id"]
    status = "NOT ASSIGNED"
    category_id = data.get("category_id",None)


    comp_id = add_new_complaint(title, description,created_by,status,category_id)

    if comp_id is not None:
        return {
            "data": {"id": comp_id}
        }, 200

    else:
        return {
            "error": {"message": "Invalid Data"}
        }, 400
    

@admin_bp.route('/update_compliant',methods=["PUT"])
@admin_only_token_required
def update_compliant(token_info):
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
    
    data = request.get_json()

    if (error := validate_update_complaint_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    id = data.get("id",None)
    title = data.get("title",None)
    description = data.get("description",None)
    category_id = data.get("category_id",None)


    comp_id = update_complaint(id,title, description,category_id)

    if comp_id is not None:
        return {
            "data": {"id": comp_id}
        }, 200

    else:
        return {
            "error": {"message": "Invalid Data"}
        }, 400


@admin_bp.route('/assign_compliant',methods=["POST"])
@admin_only_token_required
def assign_compliant(token_info):
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
    
    data = request.get_json()

    if (error := validate_assign_complaint_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    staff_id = data.get("staff_id",None)
    complaint_id = data.get("complaint_id",None)
    created_by = token_info["login_id"]


    check_staff_status = staff_status(staff_id)
    print(check_staff_status)
    if check_staff_status is not None and check_staff_status == 0 :
        assignment_id = assign_complaint_to_staff(staff_id,complaint_id,created_by)

        if assignment_id is not None:
            return {
                "data": {"id": assignment_id}
            }, 200

        else:
            return {
                "error": {"message": "Invalid Data"}
            }, 400
    
    else:
         return {
                "data": {"message": "Staff ID is blocked or deleted"}
            }, 400
    

@admin_bp.route('/change_assignee',methods=["POST"])
@admin_only_token_required
def change_assignee(token_info):
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
    
    data = request.get_json()

    if (error := validate_assign_complaint_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    staff_id = data.get("staff_id",None)
    complaint_id = data.get("complaint_id",None)
    created_by = token_info["login_id"]


    check_staff_status = staff_status(staff_id)
    print(check_staff_status)
    if check_staff_status is not None and check_staff_status == 0 :
        assignment_id = assign_complaint_to_staff(staff_id,complaint_id,created_by)

        if assignment_id is not None:
            return {
                "data": {"id": assignment_id}
            }, 200

        else:
            return {
                "error": {"message": "Invalid Data"}
            }, 400
    
    else:
         return {
                "data": {"message": "Staff ID is blocked or deleted"}
            }, 400
    
@admin_bp.route('/mark_as_completed',methods=["PUT"])
@admin_only_token_required
def mark_as_completed(token_info):
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
    
    data = request.get_json()

    if (error := validate_mark_complaint_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    complaint_id = data.get("complaint_id",None)
    created_by = token_info["login_id"]


    mark = mark_complaint_resolved(complaint_id)

    if mark is not None:
        return {
            "data": {"id": complaint_id}
        }, 200

    else:
        return {
            "error": {"message": "Failed to update data "}
        }, 400
    
    

    
