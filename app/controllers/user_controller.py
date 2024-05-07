from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from ..model.user import db, User
from flask import jsonify
import re


class UserController:

    def validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def register_user(self, data):
        required_fields = ['username', 'password', 'email',
                           'user_type']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'message': f'O campo {field} é obrigatório e não pode estar vazio.'}), 400

        if not self.validate_email(data['email']):
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
            is_vendedor = True
        else:
            if not cnpj or len(cnpj) != 14:
                return jsonify({'message': 'CNPJ deve conter 14 caracteres.'}), 400
            if cpf:
                return jsonify({'message': 'CPF não deve ser fornecido para pessoa jurídica.'}), 400
            is_vendedor = False

        hashed_password = generate_password_hash(data['password'])
        new_user = User(
            username=data['username'],
            password=hashed_password,
            email=data['email'],
            cpf=cpf if user_type == 'fisica' else None,
            cnpj=cnpj if user_type == 'juridica' else None,
            permission_level=2,
            is_vendedor=is_vendedor
        )
        db.session.add(new_user)

        try:
            db.session.commit()
            additional_claims = {'permission_level': new_user.permission_level, 'user_id': new_user.id}
            access_token = create_access_token(identity=new_user.email, additional_claims=additional_claims)
            return jsonify({'message': 'Usuário registrado com sucesso.', 'access_token': access_token}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': 'Usuário já existe.'}), 409
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': str(e)}), 500

    def login_user(self, data):
        email = data.get('email')
        password = data.get('password')

        if email is None or password is None:
            return jsonify({"msg": "Email e senha são necessários"}), 400

        if not self.validate_email(email):
            return jsonify({"msg": "Formato de email inválido"}), 400

        user = User.query.filter_by(email=email).first()

        if user and password and check_password_hash(user.password, password):
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg": "Email ou senha inválidos"}), 401
