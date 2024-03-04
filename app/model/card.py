from ..services.db import db
class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    person_type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(14), nullable=True)
    marital_status = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    monthly_income = db.Column(db.String(20), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    neighborhood = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    property_value = db.Column(db.String(20), nullable=False)
    loan_value = db.Column(db.String(20), nullable=False)
    payment_term = db.Column(db.String(50), nullable=False)
