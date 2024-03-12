from flask import Blueprint, request, jsonify
from ..services.auth_services import register_user, login_user
from flask_cors import CORS
from flask_cors import cross_origin


auth_bp = Blueprint('auth', __name__)
CORS(auth_bp)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return register_user(data)


@auth_bp.route('/login', methods=['POST'])
@cross_origin(origin='http://localhost:3000/authentication/signin',headers=['Content- Type','Authorization'])
def login():
    data = request.get_json()
    return login_user(data)

