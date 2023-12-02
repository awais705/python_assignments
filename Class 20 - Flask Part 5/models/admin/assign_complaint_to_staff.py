import db 
from datetime import date,datetime

def assign_complaint_to_staff(staff_id,complaint_id,created_by):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'INSERT INTO complaint_assign(complaint_id,staff_id,created_at,assigned_by) values (%s,%s,%s,%s)'
    cur.execute(sql , (complaint_id,staff_id,date.today(),created_by))    
    db_conn.commit()

    res = cur.lastrowid 

    if res and res is not None:
        sql = 'UPDATE complaint SET  status = %s, assigned_to = %s where id = %s'
        cur.execute(sql , ('ASSIGNED', staff_id, complaint_id))    
        db_conn.commit()
        
        return res