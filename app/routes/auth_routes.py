from flask import Blueprint, request
from flask_cors import CORS
from flask_cors import cross_origin

from app.controllers.user_controller import UserController

auth_bp = Blueprint('auth', __name__)
CORS(auth_bp, resources={r"/auth/*": {"origins": "http://localhost:3000"}}, support_credentials=True, methods=['POST', 'PUT', 'DELETE', 'OPTIONS', 'GET'])
user_controller = UserController()


@auth_bp.route('/register', methods=['POST'])
@cross_origin(supports_credentials=True)
def register():
    data = request.get_json()
    return user_controller.register_user(data)


@auth_bp.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def login():
    data = request.get_json()
    response = user_controller.login_user(data)
    return response
