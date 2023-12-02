def validate_complain_type_data(data):
    error_msg = None
    if data.get("name") is None or len(data.get("name").strip()) == 0:
        error_msg = "name field is required"
    
    return error_msg

def validate_complaint_data(data):
    error_msg = None
    if data.get("title") is None or len(data.get("title").strip()) == 0:
        error_msg = "title field is required"

    if data.get("category_id") is None or len(data.get("category_id").strip()) == 0:
        error_msg = "Category field is required"
    
    return error_msg



def validate_update_complaint_data(data):
    error_msg = None
    if data.get("id") is None or len(data.get("id").strip()) == 0:
        error_msg = "id field is required"

    
    return error_msg


def validate_assign_complaint_data(data):
    error_msg = None
    if data.get("staff_id") is None or len(data.get("staff_id").strip()) == 0:
        error_msg = "staff id field is required"

    if data.get("complaint_id") is None or len(data.get("complaint_id").strip()) == 0:
        error_msg = "complaint id field is required"

    
    return error_msg


def validate_mark_complaint_data(data):
    error_msg = None
    if data.get("complaint_id") is None or len(data.get("complaint_id").strip()) == 0:
        error_msg = "complaint id field is required"

    return error_msg