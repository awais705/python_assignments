from flask import Flask
from controllers.users.users import users_bp
from controllers.customer.customer import customer_bp
from controllers.admin.admin import admin_bp




app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(customer_bp, url_prefix="/customer")
app.register_blueprint(admin_bp, url_prefix="/admin")


if __name__  == "__main__":
    app.run(
        debug=True,
        port=3000
    )
