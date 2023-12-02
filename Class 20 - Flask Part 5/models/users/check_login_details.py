import db 
from datetime import date,datetime

def check_login_details(email, password,role):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = """SELECT id FROM users where email = %s and password = %s and user_type  = %s"""
   
    cur.execute(sql,(email,password,role))    
    db_conn.commit()

    res = cur.fetchone()
   

    if res and res.get("id") is not None:
        return {
                "id": res.get("id")  
            }
        

