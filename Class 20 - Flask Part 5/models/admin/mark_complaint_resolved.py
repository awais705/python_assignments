import db 
from datetime import date,datetime

def mark_complaint_resolved(complaint_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'UPDATE complaint SET  status = %s , resolved_date = %s  where id = %s' 
    res = cur.execute(sql , ("RESOLVED",date.today(),complaint_id))  
    db_conn.commit()
    
    return res