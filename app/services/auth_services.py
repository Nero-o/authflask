from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from ..model.user import db, users
from flask import jsonify
import re


def validate_email(email):
    # Regex simples para validação de email
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
def register_user(data):
    required_fields = ['username', 'password', 'email']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'message': f'O campo {field} é obrigatório e não pode estar vazio.'}), 400

    # Validar email
    if not validate_email(data['email']):
        return jsonify({'message': 'Formato de email inválido.'}), 400

    user_type = data['user_type']
    cpf = data.get('cpf')
    cnpj = data.get('cnpj')

    if user_type not in ['fisica', 'juridica']:
        return jsonify({'message': 'Tipo de usuário inválido.'}), 400

    if user_type == 'fisica':
        if not cpf or len(cpf) != 11:
            return jsonify({'message': 'CPF deve conter 11 caracteres.'}), 400
        if cnpj:
            return jsonify({'message': 'CNPJ não deve ser fornecido para pessoa física.'}), 400
    else:  # pessoa juridica
        if not cnpj or len(cnpj) != 14:
            return jsonify({'message': 'CNPJ deve conter 14 caracteres.'}), 400
        if cpf:
            return jsonify({'message': 'CPF não deve ser fornecido para pessoa jurídica.'}), 400

    # Criptografar senha
    hashed_password = generate_password_hash(data['password'])

    # Criar usuário
    new_user = users(
        username=data['username'],
        password=hashed_password,
        email=data['email'],
        cpf=cpf if user_type == 'fisica' else None,
        cnpj=cnpj if user_type == 'juridica' else None
    )
    db.session.add(new_user)

    try:
        db.session.commit()
        return jsonify({'message': 'Usuário registrado com sucesso.'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Usuário já existe.'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


def login_user(data):
    email = data.get('email')
    password = data.get('password')

    # Validações de campos não vazios e formato de email
    if not email or not password:
        return jsonify({"msg": "Email e senha são obrigatórios"}), 400

    if not validate_email(email):
        return jsonify({"msg": "Formato de email inválido"}), 400

    # Tenta encontrar o usuário pelo email
    user = users.query.filter_by(email=email).first()

    # Verifica se o usuário existe e se a senha está correta
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Email ou senha inválidos"}), 401