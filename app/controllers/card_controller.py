from flask import jsonify, request
from ..services.pipefy_services import create_pipefy_card
from ..model.card import Card
from .. import db


def create_card():
    data = request.get_json()

    # Cria card no pipefy
    card_data = create_pipefy_card(data)

    # Salva card no banco de dados
    new_card = Card(
        person_type=data.get('person_type'),
        name=data.get('name'),
        cpf=data.get('cpf'),
        marital_status=data.get('marital_status'),
        phone=data.get('phone'),
        email=data.get('email'),
        monthly_income=data.get('monthly_income'),
        property_type=data.get('property_type'),
        cep=data.get('cep'),
        address=data.get('address'),
        number=data.get('number'),
        neighborhood=data.get('neighborhood'),
        city=data.get('city'),
        state=data.get('state'),
        property_value=data.get('property_value'),
        loan_value=data.get('loan_value'),
        payment_term=data.get('payment_term')
    )
    db.session.add(new_card)
    db.session.commit()

    return jsonify({'message': 'Card created successfully', 'card': card_data}), 201
