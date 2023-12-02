import db 
from datetime import date,datetime

def update_user_details(id,name,email,password):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'UPDATE users SET name = Coalesce(%s,name) , email = Coalesce(%s,email), password = Coalesce(%s,password), updated_at = %s where id = %s'
    update = cur.execute(sql , (name,email,password,date.today(),id))  
    db_conn.commit()

    return update