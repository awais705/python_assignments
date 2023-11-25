def validate_search_data(term):
    error_msg = None
    if term is None or len(term.strip()) == 0:
        error_msg = "name field is required"
   
    return error_msg


def validate_pagination_data(page):
    error_msg = None
    if page is None or len(page.strip()) == 0:
        error_msg = "name field is required"
   
    return error_msg

def validate_borrow_data(data):
    error_msg = None
    if data.get("from_date") is None or len(data.get("from_date").strip()) == 0:
        error_msg = "From date field is required"
    
    if data.get("to_date") is None or len(data.get("to_date").strip()) == 0:
        error_msg = "To date field is required"

    if data.get("book_id") is None or len(data.get("book_id").strip()) == 0:
        error_msg = "Book ID field is required"
   
    return error_msg



