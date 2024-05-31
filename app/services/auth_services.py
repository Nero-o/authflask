from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from ..model.user import db, Users
from flask import jsonify, request
import re


def validate_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None


def register_user(data):
    required_fields = ['username', 'password', 'email']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'message': f'O campo {field} é obrigatório e não pode estar vazio.'}), 400

    # Validar email
    if not validate_email(data['email']):
        return jsonify({'message': 'Formato de email inválido.'}), 400

    user_type = data.get('user_type')
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
    new_user = Users(
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
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not validate_email(email):
        return jsonify({"msg": "Formato de email inválido"}), 400

    # Tenta encontrar o usuário pelo email
    user = Users.query.filter_by(email=email).first()

    # Verifica se o usuário existe e se a senha está correta
    if user and check_password_hash(user.password, password):
        additional_claims = {'email': user.email, 'name': user.username}
        access_token = create_access_token(identity=user.id, additional_claims=additional_claims)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Email ou senha inválidos"}), 401
