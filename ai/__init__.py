from flask import Flask
from ai.routes import get_routes

# Create the Flask application instance
def create_app():
    app = Flask(__name__)
    get_routes(app)
    
    return app