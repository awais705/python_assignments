import db 

def get_complaint_counts(duration = "", status=""):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()


    sql=""
    if duration == "today" and status == "":
        sql = "SELECT count(id) as total from complaint WHERE date(created_at) = date(NOW())"
    elif duration == "today" and status == "RESOLVED":
        sql = "SELECT count(id) as total from complaint WHERE date(created_at) = date(NOW()) and status= 'RESOLVED'"
    elif duration == "weekago" and status == "":
        sql = "SELECT count(id) as total from complaint WHERE date(created_at) >= (DATE(NOW() - INTERVAL 7 DAY))"
    elif duration == "weekago" and status == "RESOLVED":
        sql = "SELECT count(id) as total from complaint WHERE date(created_at) >= (DATE(NOW() - INTERVAL 7 DAY)) and status='RESOLVED'"
    elif duration == "monthago" and status == "":
        sql = "SELECT count(id) as total from complaint WHERE date(created_at) >= (DATE(NOW() - INTERVAL 30 DAY))"
    elif duration == "monthago" and status == "RESOLVED":
        sql = "SELECT count(id) as total from complaint WHERE date(created_at) >= (DATE(NOW() - INTERVAL 30 DAY)) and status='RESOLVED'"


   
    cur.execute(sql)    
    db_conn.commit()

    res = cur.fetchone()
    
    return str(res.get("total"))