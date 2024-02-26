from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from ..model.models import db, users
from flask import jsonify

def register_user(data):
    username = data['username']
    password = data['password']
    hashed_password = generate_password_hash(password)
    
    user = users(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'Registrado com sucesso'}), 200

def login_user(data):
    username = data['username']
    password = data['password']
    user = users.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Nome ou senha inválidos"}), 401