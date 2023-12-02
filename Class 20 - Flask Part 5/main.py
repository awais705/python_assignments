from flask import Flask,request
from datetime import timedelta
from controllers.users.users import users_bp
from controllers.admin.admin import admin_bp
from controllers.staff.staff import staff_bp

app = Flask(__name__)



from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


# https://flask-jwt-extended.readthedocs.io/en/stable/options.html
app.config["JWT_SECRET_KEY"] = "its-not-over-until-i-win"  # Change this!
app.config["JWT_TOKEN_LOCATION"] = ["headers"] # specifying the location of JWT 
app.config["JWT_ALGORITHM"] = "HS256" # symmetric keyed hashing algorithm
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=10)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)


app.register_blueprint(users_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(staff_bp)

# app.register_blueprint(customer_bp, url_prefix="/customer")
# app.register_blueprint(admin_bp, url_prefix="/admin")



if __name__  == "__main__":
    app.run(
        debug=True,
        port=3000
    )
