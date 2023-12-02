import db 

def get_max_user_id():
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = "SELECT MAX(id) as last_row_id from users "
    cur.execute(sql)    
    db_conn.commit()

    res = cur.fetchone()
    return res.get("last_row_id")