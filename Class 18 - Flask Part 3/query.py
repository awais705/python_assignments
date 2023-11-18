import db 
from datetime import date,datetime
#  Check login
def login_user(data):

    email = data["email"]
    password = data["password"]
    # print(password)
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = "SELECT id,email,username FROM users where email = %s and password = %s"
    # return sql
    cur.execute(sql,(email,password))    
    db_conn.commit()

    res = cur.fetchone()
    return res


# Register user
def register_user(data):
    email = data["email"]
    password = data["password"]
    fullname = data["fullname"]
    username = data["username"]

    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'INSERT INTO users(username,full_name,email,password,created_at) values (%s,%s,%s,%s,%s)'
    cur.execute(sql , (username,fullname,email,password,date.today()) )    
    db_conn.commit()

    res = cur.lastrowid 
    return res


def user_login(user_id,token):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = 'INSERT INTO user_login(user_id,access_token,created_at) values (%s,%s,%s)'
    cur.execute(sql , (user_id,token,date.today()))    
    db_conn.commit()

    res = cur.lastrowid 
    return res


#Get notes by user id
def get_notes_by_id(user_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = "SELECT * FROM notes where user_id = %s"
    cur.execute(sql , (user_id))    
    db_conn.commit()

    res = cur.fetchall()
    return res


#post notes 
def add_user_notes(data):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()


    title = data["title"] if "title" in data else 'NULL'
    desc = data["desc"] if "desc" in data else 'NULL'
    # remind_me = data["remind_me"] if "remind_me" in data else 'NULL'


    user_id = data["user_id"]
    date_time = date.today()


    sql = 'INSERT INTO notes(title,description,user_id,created_at) values (%s,%s,%s,%s)'
    cur.execute(sql , (title,desc,user_id,date_time))    
    db_conn.commit()

    res = cur.lastrowid 
    return res


# Assign category to notes
def add_notes_category(note_id,category,user_id):
    
    
    for individual in category.split(','):
        category_id = get_category_id(individual)
        assign_category_to_notes(category_id,note_id,user_id)

    return True



# category id from category table , if not exist create new and send it 
def get_category_id(category):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = "SELECT id FROM category where `name` =  %s"
    cur.execute(sql , (category))    
    db_conn.commit()

    res = cur.fetchone()
    if res is None:
        #create new category
        cat_id = create_category(category)
        return cat_id
    else:
        return res

# Create category 
def create_category(category):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    date_time = date.today()

    sql = 'INSERT INTO category(name,description,created_at) values (%s,%s,%s)'
    cur.execute(sql , (category,'',date_time))    
    db_conn.commit()

    res = cur.lastrowid 
    return res


# Assign category to note 
def assign_category_to_notes(category_id,note_id,user_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    date_time = date.today()

    check_owner = check_note_owner(note_id,user_id)
    if check_note_owner is not None:

        sql = 'INSERT INTO notes_category(notes_id,category_id,created_at) values (%s,%s,%s)'
        cur.execute(sql , (note_id,category_id,date_time))    
        db_conn.commit()

        res = cur.lastrowid 
        return res
    
    else:
        return False


#check owner of the note before inserting cateogry
def check_note_owner(note_id,user_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = "SELECT id FROM notes WHERE id=(%s) and user_id = (%s)"
    cur.execute(sql , (note_id,user_id))    
    db_conn.commit()

    res = cur.fetchone()
    return res


    


# Get user own notes as per category
def get_category_notes_by_id(user_id,cat):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    sql = """SELECT n.title,n.description,c.name FROM
      notes n inner join notes_category nc on n.id = nc.notes_id  
      inner join category c on nc.category_id = c.id WHERE n.user_id = (%s) and nc.category_id = (%s)"""
    cur.execute(sql , (user_id,cat))    
    db_conn.commit()

    res = cur.fetchall()
    return res
