import db 
from datetime import date,datetime

def mark_done_assignment(staff_id,complaint_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'UPDATE complaint SET  status = %s , resolved_date = %s  where id = %s and assigned_to=%s' 
    res = cur.execute(sql , ("RESOLVED",date.today(),complaint_id,staff_id))  
    db_conn.commit()

    return res