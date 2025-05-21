from flask import Flask
from .routes import main
from app.routes import main
from flasgger import Swagger
def create_app():
    app = Flask(__name__)
    Swagger(app)
    app.register_blueprint(main)
    
    return app