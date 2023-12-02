import db 
from datetime import date,datetime

def add_new_complaint(title, description,created_by,status,category_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'INSERT INTO complaint(title,description,status,created_at,created_by,category_id) values (%s,%s,%s,%s,%s,%s)'
    cur.execute(sql , (title,description,status,date.today(),created_by,category_id))    
    db_conn.commit()

    res = cur.lastrowid 
    return res