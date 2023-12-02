import db 
from datetime import date,datetime

def update_complaint(id,title, description,category_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'UPDATE complaint SET title = Coalesce(%s,title) , description = Coalesce(%s,description), category_id = Coalesce(%s,category_id) where id = %s'
    update = cur.execute(sql , (title,description,category_id,id))  
    db_conn.commit()

    return update

