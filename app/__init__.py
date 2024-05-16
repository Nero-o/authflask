from flask import Flask
from .model.user import db
from .routes.auth_routes import auth_bp
from .routes import cards_routes
from config import Config
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate  # Import Migrate
from flask_cors import CORS
import pymysql

pymysql.install_as_MySQLdb()


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(Config)

    jwt = JWTManager(app)
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(cards_routes.card_bp, url_prefix='/api')

    return app
