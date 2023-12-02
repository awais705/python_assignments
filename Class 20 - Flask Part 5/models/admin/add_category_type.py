import db 
from datetime import date,datetime

def add_category_type(name, description,created_by):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'INSERT INTO complaint_category(name,description,created_at,created_by) values (%s,%s,%s,%s)'
    cur.execute(sql , (name,description,date.today(),created_by))    
    db_conn.commit()

    res = cur.lastrowid 
    return res



