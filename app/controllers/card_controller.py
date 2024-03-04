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
        tipo_pessoa=data.get('person_type'),
        nome=data.get('name'),
        cpf_cnpj=data.get('cpf'),
        estado_civil=data.get('marital_status'),
        telefone=data.get('phone'),
        email=data.get('email'),
        renda_mensal=data.get('monthly_income'),
        tipo_terreno=data.get('property_type'),
        cep=data.get('cep'),
        endereco=data.get('address'),
        numero=data.get('number'),
        bairro=data.get('neighborhood'),
        cidade=data.get('city'),
        estado=data.get('state'),
        valor_propriedade=data.get('property_value'),
        valor_emprestimo=data.get('loan_value'),
        prazo_pagamento=data.get('payment_term')
    )
    db.session.add(new_card)
    db.session.commit()

    return jsonify({'message': 'Card created successfully', 'card': card_data}), 201
