# Script to create Flask app, sets up SQLAlchemy instance, register blueprints for different API endpoints
# create database tables, and set up login manager

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Create a new SQLAlchemy instance
db = SQLAlchemy()
# Set the name of the database file
DB_NAME = "database.db"

# Function to create a new Flask application instance
def create_app():
    """ Create Flask app """
    app = Flask(__name__)

    # Configure the app's settings
    app.config['SECRET_KEY'] = 'secret'  # App's secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # URI for db, to be reconfigured with mysql
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications to improve performance
    db.init_app(app)  # Initialize the app's SQLAlchemy instance

    # Register the app's blueprints for different API endpoints
    from .api.auth import auth
    from .api.views import views

    app.register_blueprint(auth)  # Register the blueprint for authentication-related endpoints
    app.register_blueprint(views)  # Register the blueprint for views

    # Import the app's user model
    from .models.user import User

    # Create the necessary tables in the database
    with app.app_context():
        # db.drop_all()
        db.create_all()

    """Manage Login"""
    login_manager = LoginManager()
    login_manager.login_view = 'auth.index'  # Endpoint for login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """ Return app instance """
        return User.query.get(str(id))


    return app

