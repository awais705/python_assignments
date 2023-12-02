import db 
from datetime import date,datetime

def get_done_assignments(staff_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'SELECT * FROM complaint WHERE assigned_to = %s and status = "RESOLVED" AND resolved_date is not null'
    cur.execute(sql , (staff_id) )
    db_conn.commit()

    res = cur.fetchall()
    return res
