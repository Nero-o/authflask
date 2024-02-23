from flask import Flask
from .model.models import db
from .routes.auth_routes import auth_bp
from config import Config
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    jwt = JWTManager(app)
    db.init_app(app)
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app
