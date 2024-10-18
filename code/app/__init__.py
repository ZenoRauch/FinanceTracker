from flask import Flask
from .models import db
from .routes import main


def create_app():
    app = Flask(__name__, template_folder="../templates")

    # Database configuration (assuming MariaDB with root user and no password)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/financetracker'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Used for session management, flash messages, etc.
    app.secret_key = 'supersecretkey'

    db.init_app(app)
    app.register_blueprint(main)

    # Import routes (controllers)
    return app
