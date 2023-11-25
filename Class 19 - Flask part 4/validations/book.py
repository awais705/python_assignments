def validate_book_info(data):
    error_msg = None
    if data.get("name") is None or len(data.get("name").strip()) == 0:
        error_msg = "name field is required"
    if data.get("description") is None or len(data.get("description").strip()) == 0:
        error_msg = "description field is required"
    if data.get("category") is None or len(data.get("category").strip()) == 0:
        error_msg = "category field is required"
    
    return error_msg


def validate_accept_borrow_data(data):
    error_msg = None
    if data.get("borrow_id") is None or len(data.get("borrow_id").strip()) == 0:
        error_msg = "Borrow Id field is required"
    
    
    return error_msg


def validate_mark_borrow_data(data):
    error_msg = None
    if data.get("borrow_id") is None or len(data.get("borrow_id").strip()) == 0:
        error_msg = "Borrow Id field is required"
    
    
    return error_msg


