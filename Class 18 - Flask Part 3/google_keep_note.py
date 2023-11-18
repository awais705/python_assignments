from flask import Flask, jsonify,request,make_response

from datetime import date,datetime,timedelta

from controller.google_notes import login,register,notes,category
# import jwt

app = Flask(__name__)
app.config["SECRET_KEY"] = "ITSNOTOVERUNTILIWIN"

# register the user

# login the user with email and password
app.add_url_rule('/login',view_func=login, methods=["POST"])


# Register User 
app.add_url_rule('/register',view_func = register, methods=["POST"])


#create notes
app.add_url_rule('/notes',view_func = notes, methods=["GET","POST"])


#create category
app.add_url_rule('/category',view_func = category, methods=["GET","POST"])



if __name__ == "__main__":
    app.run(debug=True, port=3000)