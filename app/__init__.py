# Import necessary modules from Flask and Flask-PyMongo
from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config  # Import the app's configuration

# Initialize the PyMongo object to interact with MongoDB
mongo = PyMongo()

# Function to create and configure the Flask application
def create_app():
    # Create a new Flask application instance
    app = Flask(__name__)

    # Load the configuration from the Config object defined in app.config
    app.config.from_object(Config)

    # Initialize the MongoDB connection with the Flask app
    mongo.init_app(app)

    # Import and register the user blueprint (routes for the user)
    from app.routes import user_bp
    app.register_blueprint(user_bp)

    # Return the configured Flask app instance
    return app
