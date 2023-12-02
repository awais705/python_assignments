import db 
from datetime import date,datetime
# from models.users.get_max_user_id
import random
import string

def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def add_new_user(name, email, password,role,created_by = 1):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    staff_number = ""
    if role == "STAFF":
        rand=random.randint(0,5000)
        staff_number = email.split("@")[0] + str(rand)

    
    

    sql = 'INSERT INTO users(name,email,password,staff_number,user_type,created_at,created_by) values (%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(sql , (name,email,password,staff_number,role,date.today(),created_by))    
    db_conn.commit()

    res = cur.lastrowid 
    return res



