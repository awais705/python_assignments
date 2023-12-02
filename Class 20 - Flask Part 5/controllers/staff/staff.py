from flask import Blueprint,request
from datetime import date,datetime
from models.staff.get_done_assignments import get_done_assignments
from models.staff.get_pending_assignments import get_pending_assignments
from models.staff.mark_done_assignment import mark_done_assignment
from models.staff.upload_doc_for_mark_done import upload_doc_for_mark_done
from models.staff.verify_staff_ownership import verify_staff_ownership
from services.token_services import staff_only_token_required, staff_token_required
from validations.admins import validate_mark_complaint_data



staff_bp = Blueprint("staffbp",__name__)

@staff_bp.route('/pending_assignments', methods=["GET"])
@staff_token_required
def pending_assignments(token_info):
  
    staff_id = token_info["login_id"]

    list_assignment = get_pending_assignments(staff_id)

    if list_assignment is not None:
        return {
            "data": {"data": list_assignment}
        }, 200

    else:
        return {
            "error": {"message": "Invalid Data"}
        }, 400


@staff_bp.route('/done_assignments', methods=["GET"])
@staff_token_required
def done_assignments(token_info):
  
    staff_id = token_info["login_id"]

    done_assignment = get_done_assignments(staff_id)

    if done_assignment is not None:
        return {
            "data": {"data": done_assignment}
        }, 200

    else:
        return {
            "error": {"message": "Invalid Data"}
        }, 400


@staff_bp.route('/mark_done', methods=["POST"])
@staff_token_required
def mark_done(token_info):
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
  
    staff_id = token_info["login_id"],
    complaint_id = data.get("complaint_id")


    verify_ownership = verify_staff_ownership(staff_id,complaint_id)
    if verify_ownership is not None:
        mark = mark_done_assignment(staff_id,complaint_id)

        if mark is not None:
            return {
                "data": {"data": mark}
            }, 200

        else:
            return {
                "error": {"message": "Invalid Data"}
            }, 400



@staff_bp.route("/upload",methods=["POST"])
@staff_only_token_required
def upload_doc(token_info):
    # data = request.get_json()
    # complaint_id = data.get("complaint_id")
    # image=request.files['image']
    # image_name=image.filename
    # return image_name
    complaint_id =  request.form["complaint_id"]
    staff_id = token_info["login_id"]


    try:
        if request.method=='POST':
            image=request.files['image']
            image_name=image.filename
            if '.jpg' or '.jpeg' in image_name:
                image.save(image_name)

                update_img = upload_doc_for_mark_done(image_name,staff_id,complaint_id)
                return {
                    "data":{"data": update_img}
                }
                
            else:
                return {"error":"select you image file"}
    except Exception as e:
        return {"error":str(e)}
