from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    class User(db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(50), unique=True, nullable=False)
        password = db.Column(db.String(255), nullable=False)
        email = db.Column(db.String(100), unique=True, nullable=False)
        cpf = db.Column(db.String(11), unique=True, nullable=True)
        cnpj = db.Column(db.String(14), unique=True, nullable=True)

