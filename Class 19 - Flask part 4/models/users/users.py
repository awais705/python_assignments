import db 
from datetime import date,datetime

def add_new_customer(name, email, password):
    
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'INSERT INTO user(name,email,password,created_at) values (%s,%s,%s,%s)'
    cur.execute(sql , (name,email,password,date.today()))    
    db_conn.commit()

    res = cur.lastrowid 
    return res

def get_role_id(role):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = "SELECT id FROM roles where name = %s"
    cur.execute(sql , (role))    
    db_conn.commit()

    res = cur.fetchone()
    return res.get("id")

def add_user_role(user_id,role_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    role_key = str(user_id) + str(role_id)

    sql = 'INSERT INTO user_role(user_id,role_id,role_key,created_at) values (%s,%s,%s,%s)'
    cur.execute(sql , (user_id, role_id, role_key, date.today()))    
    db_conn.commit()

    res = cur.lastrowid 
    return res


def check_login_details(email,password,role):

    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = """SELECT id FROM user where email = %s and password = %s"""
   
    cur.execute(sql,(email,password))    
    db_conn.commit()

    res = cur.fetchone()
   

    if res and res.get("id") is not None:
        user_id = res.get("id")
        role_id = get_role_id(role)
        user_role = check_user_role(user_id,role_id)
        if user_role is not None:
            return {
                "id": user_id  
            }
        



def check_user_role(user_id,role_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = "SELECT id FROM user_role WHERE user_id = %s AND  role_id = %s"
    cur.execute(sql , (user_id,role_id))    
    db_conn.commit()

    res = cur.fetchone()
    return res.get("id")




