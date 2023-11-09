from flask import Flask, request
import db
from datetime import date
import json

app = Flask(__name__)

# create a flask application that should be able to signup, login and display all users
# APIs
# - POST: /register
# - GET: /users
# - PATCH: /change-password
# - POST: /login

# Responses
# /register: "user added successfully"
# /change-password: "password updated successfully"
# /login: "user login successfully"
# /users: {
#   "id": int,
#   "name": string,
#   "email": string,
#   "dob": string,
#   "phone": string,
#   "created_at": string
# }


@app.route('/')
def index():
    return "Hello World"




# Signup
@app.route('/register', methods=['POST'])
def register_user():
    
    if request.method == "POST":
        db_conn = db.mysqlconnect()
        cur = db_conn.cursor()

        if 'name' in request.form and 'password' in request.form and 'email' in request.form and 'dob' in request.form and 'phone' in request.form:
            name = request.form["name"]
            password = request.form["password"]
            email = request.form["email"]
            dob = request.form["dob"]
            phone = request.form["phone"]


            sql1 = 'INSERT INTO user(name,password,email,dob,phone,created_at) values (%s,%s,%s,%s,%s,%s)'
            cur.execute(sql1 , (name,password,email,dob,phone,date.today()) )

            db_conn.commit()

            return "user added successfully"


        else:
            return "Required fields are missing"
        

# Login
@app.route('/login', methods=["POST"])
def login_user():
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    if 'email' in request.form and 'password' in request.form:
        email = request.form["email"]
        password = request.form["password"]

        sql = "SELECT email FROM user where email = %s and password = %s"

        db_conn.commit()
        cur.execute(sql , (email,password) )

        res = cur.fetchone()
        # print(res)
        if res  != None:
            return "User is logged in "
        else:
            return "User details are invalid!"

    


# display users
@app.route('/users', methods=["GET"])
def users():
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM user")
    result = cur.fetchall()
    return result
    # print(json.dumps(result))


# change password


@app.route('/change-password/<id>', methods=["PATCH"])
def change_password(id):
   
    db_conn = db.mysqlconnect()
    cur = db_conn.cursor()

    new_password = ""
    if request.form["password"]:
        new_password = request.form["password"]
   

    if request.method == "PATCH" and new_password:
        # return "In"
        sql = "UPDATE user SET password = %s WHERE id = %s"
        cur.execute(sql,(new_password,id))

        db_conn.commit()

        return f"Password Updated successfully for ID : {id}"


if __name__ == "__main__":
    app.run(debug=True)
