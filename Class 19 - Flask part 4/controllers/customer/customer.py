from flask import Blueprint,request
from validations.customer import validate_search_data, validate_pagination_data,validate_borrow_data
from models.books.books import search_books,get_books, add_borrow_request
from services import token_services 

customer_bp = Blueprint("customerbp",__name__)

@customer_bp.route("/")
def index():
    return "Welcome to Library Management System"

@customer_bp.route("/search",methods=["GET"])
def search_book():
    term = request.args.get('q')
    if (error := validate_search_data(term)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    
    books = search_books(term)

    if books is not None:
        
        return {
            "books": books
        }, 200
    
    else:
        return {
            "books": []
        }, 200

@customer_bp.route("/book_listing",methods=["GET"])
def show_pagination():
    page = request.args.get('p')
    per_page = 5

    if (error := validate_pagination_data(page)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    book_data = get_books(page,per_page)

    if book_data is not None:
    
        return {
            "books": book_data
        }, 200
    
    else:
        return {
            "books": []
        }, 200


@customer_bp.route('/borrow_book',methods=["POST"])
@token_services.token_required
def borrow(user):
    if not request.is_json:
        return {
            "error": {
                "message": "API expect json. Please provide Json data"
            }
        }, 400
    
    data = request.get_json()
    if (error := validate_borrow_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    
    book_id = data.get("book_id")
    to_date = data.get("to_date")
    from_date = data.get("from_date")
    user_id = user['user_id']

    borrow_id = add_borrow_request(book_id, to_date, from_date,user_id)

    if borrow_id is not None:
        return {
            "data": {"borrow_id": borrow_id}
        }, 200




