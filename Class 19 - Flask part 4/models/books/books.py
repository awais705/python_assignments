import db 
from datetime import date,datetime

def search_books(query):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    query = "%" + query +"%"


    sql = "SELECT * FROM books where name like %s or description like %s or category like %s"
    cur.execute(sql , (query,query,query))    
    db_conn.commit()

    res = cur.fetchall()
    return res


def add_new_book(name, description, category,admin_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()
    
    date_time = date.today()

    sql = 'INSERT INTO books(name,description,category,added_by,created_at) values (%s,%s,%s,%s,%s)'
    cur.execute(sql , (name,description,category,admin_id,date_time))    
    db_conn.commit()

    res = cur.lastrowid 
    return res


def get_books(page,per_page=5):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    offset  =   (int(page) - 1) * 5

    sql = "SELECT * FROM books limit %s offset %s"
    cur.execute(sql , (per_page,offset))    
    db_conn.commit()

    res = cur.fetchall()
    return res

def add_borrow_request(book_id, to_date, from_date,user_id):

    status = "PENDING"
    return_date = "1971-01-01"

    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()
    
    date_time = date.today()

    sql = """INSERT INTO book_borrow(book_id,user_id,from_date,to_date,status,return_date,created_at) values (%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(sql , (book_id,user_id,from_date,to_date,status,return_date,date_time))    
    db_conn.commit()

    res = cur.lastrowid 
    return res


def accept_borrowing_request(borrow_id):

    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    status = 'BORROWED'


    sql = """UPDATE book_borrow SET status = %s WHERE id = %s"""
    cur.execute(sql , (status,borrow_id))    
    db_conn.commit()

    return cur.rowcount

def get_list_borrowing(list_type):

    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()


    if list_type == "ALL":
        sql = "select b.id as borrow_id, b.id as book_id,b.name as book_name, u.name as user_name,bb.status as status, bb.to_date as to_date, bb.from_date as from_date from book_borrow bb inner join books b on bb.book_id = b.id inner join user u on bb.user_id = u.id"
        cur.execute(sql)  
    else:
        sql = "select b.id as borrow_id, b.id as book_id,b.name as book_name, u.name as user_name,bb.status as status, bb.to_date as to_date, bb.from_date as from_date from book_borrow bb inner join books b on bb.book_id = b.id inner join user u on bb.user_id = u.id  where bb.status = %s"
        cur.execute(sql , (list_type))  
   
    db_conn.commit()

    res = cur.fetchall()
    return res


def marked_as_returned(borrow_id):
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    status = 'RETURNED'
    date_time = date.today()

    sql = """UPDATE book_borrow SET `status` = %s , return_date = %s WHERE id = %s"""
    
    cur.execute(sql , (status,date_time,borrow_id))    
    db_conn.commit()

    return cur.rowcount 
    


