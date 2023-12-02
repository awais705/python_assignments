import db 
from datetime import date,datetime

def staff_status(staff_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'SELECT is_deleted as status  from users where id = %s and user_type = "STAFF"'
    cur.execute(sql , (staff_id) )
    db_conn.commit()

    res = cur.fetchone()
    return res.get("status")