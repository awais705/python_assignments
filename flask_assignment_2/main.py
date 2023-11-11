import logging
logging.basicConfig(level=logging.DEBUG)
import json


from flask import Flask, abort, make_response, request

from mysql import db

app = Flask(__name__)
log = logging.getLogger("flask-app")


@app.route("/employee", methods=['GET'])
def get_employees():
    log.info("get all employees")

    conn = db.mysqlconnect()
    employees = db.get_all_employees(conn)
    db.disconnect(conn)
    
    if len(employees) == 0:
        log.warning("employee not found")
        return {
            "data": [],
            "message": "employee not found"
        }, 200

    return {
        "data": employees
    }, 200


@app.route("/employee/<user_id>", methods=['GET'])
def get_employee_profile(user_id):
    print("user_id", user_id)
    if user_id.isdigit() == False or int(user_id) <= 0:
        log.error("invalid ID")
        return {
            "error": {"message": "invalid id"}
        }, 400

    conn = db.mysqlconnect()
    employee = db.get_employee_by_id(conn, user_id)
    db.disconnect(conn)

    if employee is None:
        log.warning("employee not found")
        return {
            "error": {"message": "employee not found"}
        }, 400

    return {
        "data": employee
    }, 200


def is_valid_employee_data(data):
    error_msg = None

    if data.get("fname") is None or len(data.get("fname").strip()) == 0:
        error_msg = "fname field is required"

    if data.get("lname") is None or len(data.get("lname").strip()) == 0:
        error_msg = "lname field is required"

    if data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"

    return error_msg

@app.route("/employee", methods=['POST'])
def add_new_employee():
    if not request.is_json:
        return {
            "error": {"message": "API Accepts json data"}
        }, 400
    
    data = request.get_json()
    if (error := is_valid_employee_data(data)) is not None:
        return {
            "error": {"message": error}
        }, 400
    
    conn = db.mysqlconnect()
    employee_id = db.add_new_employee(conn, data)
    db.disconnect(conn)

    log.info("new employee added")
    return {
        "data": {"id": employee_id}
    }, 200


# Extend the existing application that contains the APIs to create and display single and all employees.
# Add following functionality to the app
# - create customer
# {
#         "fname": "Abdul",
#         "lname": "Ahad",
#         "employee_id": 7,
#         "phone": "03422766346",
#         "city": "Karachi",
#         "country": "Pakistan",
#         "language": "Urdu",
#         "lead_generated_at": "2023-11-11"
#     }


@app.route('/customer',methods=["POST"])
def add_customer():
    if not request.is_json:
        return {
            "error": {"message": "API Accepts json data"}
        }, 400
    
    data = request.get_json()
    
    conn = db.mysqlconnect()
    customer_id = db.add_new_customer(conn, data)
    db.disconnect(conn)

    log.info("new customer added")
    return {
        "data": {"id": customer_id}
    }, 200


# show all customers
#  # This endpoint should also allow filtering using query string i.e ?employee_id=1123123 and also with customer name

@app.route('/customer',methods=["GET"])
def show_all_customer():
    log.info("get all customers")

    conn = db.mysqlconnect()
    customers = db.get_all_customers(conn)
    db.disconnect(conn)
    
    if len(customers) == 0:
        log.warning("customers not found")
        return {
            "data": [],
            "message": "customers not found"
        }, 200

    return {
        "data": customers
    }, 200
    


# - display 1 customer by its id
@app.route('/customer/<int:customer_id>',methods=["GET"])
def show_individual_customer(customer_id):
    print("customer_id", customer_id)
    if customer_id.isdigit() == False or int(customer_id) <= 0:
        log.error("invalid ID")
        return {
            "error": {"message": "invalid id"}
        }, 400

    conn = db.mysqlconnect()
    customer = db.get_customer_by_id(conn, customer_id)
    db.disconnect(conn)

    if customer is None:
        log.warning("customer not found")
        return {
            "error": {"message": "customer not found"}
        }, 400

    return {
        "data": customer
    }, 200


# - DELETE CUSTOMER 
@app.route('/customer/<int:customer_id>',methods=["DELETE"])
def delete_individual_customer(customer_id):
    print("customer_id", customer_id)
    if int(customer_id) <= 0:
        log.error("invalid ID")
        return {
            "error": {"message": "invalid id"}
        }, 400

    conn = db.mysqlconnect()
    delete = db.delete_customer_by_id(conn, customer_id)
    db.disconnect(conn)
    

    return {
            "data": {"message": "Customer Deleted succesfully"}
        }, 200

    

# - allow customer to puchase service
@app.route('/service',methods=["POST"])
def add_service():
    if not request.is_json:
        return {
            "error": {"message": "API Accepts json data"}
        }, 400
    
    data = request.get_json()
    
    conn = db.mysqlconnect()
    service_id = db.add_new_service(conn, data)
    db.disconnect(conn)

    log.info("new service added")
    return {
        "data": {"id": service_id}
    }, 200

# - allow customer to add payment against the service
# {
#       "customer_id": 2,
#       "order_date": "2023-11-11",
#       "status": "Shipped",
#       "comments": "Lorum Ipsum",
#       "created_at": "2023-11-11",
#       "service_id": 2
#     }
@app.route('/order',methods=["POST"])
def add_payment():
    if not request.is_json:
        return {
            "error": {"message": "API Accepts json data"}
        }, 400
    
    data = request.get_json()
    
    conn = db.mysqlconnect()
    order_id = db.add_new_order(conn, data)
    db.disconnect(conn)

    log.info("new order added")
    return {
        "data": {"id": order_id}
    }, 200



# - display all customers of 1 employee
@app.route('/employee_customer/<int:employee_id>',methods=["GET"])
def employee_customer(employee_id):
    log.info("get all customers")

    conn = db.mysqlconnect()
    customers = db.get_all_employee_customers(conn,employee_id)
    db.disconnect(conn)
    
    if len(customers) == 0:
        log.warning("employee customers not found")
        return {
            "data": [],
            "message": "employee customers not found"
        }, 200

    return {
        "data": customers
    }, 200
    




app.run(
    debug=True,
    port=3000
)
