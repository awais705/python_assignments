from flask import Blueprint,request
from validations.book import validate_book_info, validate_accept_borrow_data,validate_mark_borrow_data
from models.books.books import add_new_book, accept_borrowing_request,get_list_borrowing,marked_as_returned
from services import token_services 

from datetime import date,datetime


admin_bp = Blueprint("adminbp",__name__)

@admin_bp.route("/")
def index():
    return "Welcome to Library Management System"


@admin_bp.route("/add_book", methods=["POST"])
@token_services.token_required
def add_book(user):
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
   
    data = request.get_json()
   
    if (error := validate_book_info(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
   
    
    name = data.get("name")
    description = data.get("description")
    category = data.get("category")
    admin_id = user['user_id']
   
   
    book_id = add_new_book(name, description, category,admin_id)

    if book_id is not None:
        
        return {
            "id": book_id
        }, 200
    
    else:
         return {
            "error": {
                "message": "Failed to add book"
            }
        }, 400
   
    

@admin_bp.route("/accept", methods=["POST"])
@token_services.token_required
def accept_borrow_req(user):
     if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
     
     data = request.get_json()

     borrow_id = data["borrow_id"]
   
     if (error := validate_accept_borrow_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
     
     
     accept = accept_borrowing_request(borrow_id)

     if accept is None :
        return {
            "error": {
                "message": "Failed to update data"
            }
        }, 400
     
     else:
         return {
            "rows_updated": accept,
            "borrow_id" : borrow_id

        }, 200
     

@admin_bp.route("/borrow_listing", methods=["GET"])
@token_services.token_required  
def get_borrow_listing(user):
    list_type = request.args.get("type")

    # user_id = user["user_id"]
    if list_type is not None:
        list_borrow = get_list_borrowing(list_type)
        return {
            "data": list_borrow,
            

        }, 200

    else:
        return {
            "error": {
                "message": "Please define type"
            }
        }, 400
    

@admin_bp.route("/mark_return", methods=["POST"])
@token_services.token_required  
def set_book_marked_returned(user):
    data = request.get_json()

    if (error := validate_mark_borrow_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    borrow_id = data["borrow_id"]

    user_id = user["user_id"]


    if user_id and borrow_id:
        update_status  = marked_as_returned(borrow_id)
    
        if update_status is not None:
            return {
            "rows_updated": update_status,
            "borrow_id" : borrow_id

        }, 200

        else:
            return {
                "error": {
                    "message": "Please provide borrow Id"
                }
            }, 400


     
