import db 
from datetime import date,datetime

def verify_staff_ownership(staff_id,complaint_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'SELECT * FROM complaint WHERE assigned_to = %s and id = %s '
    cur.execute(sql , (staff_id,complaint_id) )
    db_conn.commit()

    res = cur.fetchone()
    return res