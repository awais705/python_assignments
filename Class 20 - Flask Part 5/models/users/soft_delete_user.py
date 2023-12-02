import db 
from datetime import date,datetime

def soft_delete_user(id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'UPDATE users SET is_deleted = 1, updated_at = %s where id = %s'
    delete = cur.execute(sql , (date.today(),id))  
    db_conn.commit()

    return delete

