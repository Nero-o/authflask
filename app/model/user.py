from ..services.db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=True)
    cnpj = db.Column(db.String(14), unique=True, nullable=True)
    permission_level = db.Column(db.String(20), nullable=False)
    is_vendedor = db.Column(db.Boolean, nullable=False, default=False)


def serialize(self):
    return {
        'id': self.id,
        'username': self.username,
        'password': self.password,
        'email': self.email,
        'cpf': self.cpf,
        'cnpj': self.cnpj,
        'is_vendedor': self.is_vendedor,
        'permission_level': self.permission_level,
    }
