import db 
from datetime import date,datetime

def upload_doc_for_mark_done(image_name,staff_id,complaint_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'UPDATE complaint SET  upload_doc = %s  where id = %s and assigned_to=%s' 
    res = cur.execute(sql , (image_name,complaint_id,staff_id))  
    db_conn.commit()

    return res