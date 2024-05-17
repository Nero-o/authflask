from flask import Blueprint, request
from ..services.auth_services import register_user, login_user
from flask_cors import CORS

auth_bp = Blueprint('auth', __name__)
CORS(auth_bp)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return register_user(data)


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_user(data)
