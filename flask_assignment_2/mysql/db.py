import pymysql


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="admin", # empty password
        db='mydb',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("db connected")
    return conn

def disconnect(conn):
  conn.close()


def get_all_employees(db_conn):
   # fetch data from db
    query = "SELECT * FROM employee"
    cur = db_conn.cursor()
    cur.execute(query)
    
    return cur.fetchall()
    

def get_employee_by_id(db_conn, employee_id):
   # fetch data from db
    query = f"SELECT * FROM employee WHERE id=%(employee_id)s"
    cur = db_conn.cursor()
    cur.execute(query, {
        "employee_id": employee_id
    })
    
    return cur.fetchone()

def add_new_employee(db_conn, data):
    # add record into databse
    query = f"""
                INSERT INTO employee (fname, lname, email, manager_id, job_title) 
                VALUES (%(fname)s, %(lname)s, %(email)s, %(manager_id)s, %(job_title)s)
            """
    cur = db_conn.cursor()
    cur.execute(query, {
        "fname": data.get("fname"),
        "lname": data.get("lname"),
        "email": data.get("email"),
        "manager_id": data.get("manager_id", 0),
        "job_title": data.get("job_title"),
    })
    
    # save the changes permanently
    db_conn.commit()
    
    return cur.lastrowid


def add_new_customer(db_conn, data):
    # add record into databse
    query = f"""
                INSERT INTO customer (fname, lname, employee_id, phone, city,country,language,lead_generated_at) 
                VALUES (%(fname)s, %(lname)s, %(employee_id)s, %(phone)s, %(city)s, %(country)s, %(language)s, %(lead_generated_at)s)
            """
    cur = db_conn.cursor()
    cur.execute(query, {
        "fname": data.get("fname"),
        "lname": data.get("lname"),
        "employee_id": data.get("employee_id"),
        "phone": data.get("phone"),
        "city": data.get("city"),
        "country": data.get("country"),
        "language": data.get("language"),
        "lead_generated_at": data.get("lead_generated_at")
    })
    
    # save the changes permanently
    db_conn.commit()
    
    return cur.lastrowid


def get_all_customers(db_conn):
   # fetch data from db
    query = "SELECT * FROM customers"
    cur = db_conn.cursor()
    cur.execute(query)
    
    return cur.fetchall()
 

def get_customer_by_id(db_conn, customer_id):
   # fetch data from db
    query = f"SELECT * FROM customer WHERE id=%(customer_id)s"
    cur = db_conn.cursor()
    cur.execute(query, {
        "customer_id": customer_id
    })


def delete_customer_by_id(db_conn,customer_id):
    query = f"DELETE FROM customer WHERE id=%(customer_id)s" 
    cur = db_conn.cursor()
    cur.execute(query, {
        "customer_id": customer_id
    })

    # save the changes permanently
    db_conn.commit()




def add_new_service(db_conn, data):
    # add record into databse

    #imput in postman 
    # {
    #     "name": "DSL Internet",
    #     "price": 1500,
    #     "created_at": "2023-11-11 01:02:30"
    # }

    
    query = f"""
                INSERT INTO service (name, price, created_at) 
                VALUES (%(name)s, %(price)s, %(created_at)s)
            """
    cur = db_conn.cursor()
    cur.execute(query, {
        "name": data.get("name"),
        "price": data.get("price"),
        "created_at": data.get("created_at")
        })
    
    # save the changes permanently
    db_conn.commit()
    
    return cur.lastrowid



def add_new_order(db_conn, data):
    # add record into databse

    #input in postman 
    # {
    #     "name": "DSL Internet",
    #     "price": 1500,
    #     "created_at": "2023-11-11 01:02:30"
    # }

    
    query = f"""
                INSERT INTO order (customer_id, order_date, status, comments, created_at, service_id) VALUES (%(customer_id)s, %(order_date)s, %(status)s, %(comments)s, %(created_at)s,%(service_id)s)
            """
    
    # print(query)
    cur = db_conn.cursor()
    cur.execute(query, {
        "customer_id": data.get("customer_id"),
        "order_date": data.get("order_date"),
        "status": data.get("status"),
        "comments": data.get("comments"),
        "created_at": data.get("created_at"),
        "service_id": data.get("service_id")
        })
    
    # save the changes permanently
    db_conn.commit()
    
    return cur.lastrowid

def get_all_employee_customers(db_conn,employee_id):
   # fetch data from db
    query = "SELECT * FROM customer where employee_id=%(employee_id)s"
    cur = db_conn.cursor()
    cur.execute(query,{
        "employee_id": employee_id,
        
        })
    
    return cur.fetchall()


