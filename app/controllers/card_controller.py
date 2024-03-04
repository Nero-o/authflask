import re

from flask import jsonify, request

from ..model.approved_cards import ApprovedCard
from ..services.pipefy_services import create_pipefy_card
from ..model.card import Card
from .. import db

def is_email_valid(email):
    # Regex simples para validação de e-mail
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def create_card(data):
    required_fields = ['tipo_pessoa', 'nome', 'cpf_cnpj', 'estado_civil', 'telefone', 'email', 'renda_mensal',
                       'tipo_terreno', 'cep', 'endereco', 'numero', 'bairro', 'cidade', 'estado', 'valor_propriedade',
                       'valor_emprestimo', 'prazo_pagamento', 'status']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'O campo {field} é obrigatório e não pode estar vazio.'}), 400

    # Valida o valor da propriedade
    valor_propriedade = float(data.get('valor_propriedade', 0))
    if not (98000 <= valor_propriedade <= 60000000):
        return jsonify({'error': 'O valor da propriedade deve estar entre R$ 98.000 e R$ 60.000.000.'}), 400

    # Valida o prazo de pagamento
    prazo_pagamento = int(data.get('prazo_pagamento', 0))
    if not (36 <= prazo_pagamento <= 240):
        return jsonify({'error': 'O prazo de pagamento deve estar entre 36 e 240 meses.'}), 400

    # Valida o formato do e-mail
    email = data.get('email')
    if not is_email_valid(email):
        return jsonify({'error': 'O formato do e-mail é inválido.'}), 400

    # Cria card no pipefy
    # card_data = create_pipefy_card(data)

    # Salva card no banco de dados
    new_card = Card(
        tipo_pessoa=data.get('tipo_pessoa'),
        nome=data.get('nome'),
        cpf_cnpj=data.get('cpf_cnpj'),
        estado_civil=data.get('estado_civil'),
        telefone=data.get('telefone'),
        email=data.get('email'),
        renda_mensal=data.get('renda_mensal'),
        tipo_terreno=data.get('tipo_terreno'),
        cep=data.get('cep'),
        endereco=data.get('endereco'),
        numero=data.get('numero'),
        bairro=data.get('bairro'),
        cidade=data.get('cidade'),
        estado=data.get('estado'),
        valor_propriedade=data.get('valor_propriedade'),
        valor_emprestimo=data.get('valor_emprestimo'),
        prazo_pagamento=data.get('prazo_pagamento'),
        status=data.get('status')
    )
    db.session.add(new_card)
    db.session.commit()

    return jsonify({'message': 'Card criado com sucesso', 'card': new_card.to_dict()}), 201

def get_cards():
    cards = Card.query.all()
    cards_list = [card.to_dict() for card in cards]
    return jsonify(cards_list), 200

def approve_card(card_id):
    card = Card.query.get(card_id)
    if card is None:
        return jsonify({'error': 'Card não encontrado.'}), 404

    # Cria um novo ApprovedCard com os dados do card
    approved_card = ApprovedCard(**card.to_dict())
    db.session.add(approved_card)

    # Exclui o card original da tabela de cards
    db.session.delete(card)

    # Salva as alterações no banco de dados
    db.session.commit()

    return jsonify({'message': 'Card movido para aprovados com sucesso.'}), 200
def update_card_status(card_id, new_status):
    card = Card.query.get(card_id)
    if not card:
        raise Exception('Card não encontrado')

    card.status = new_status

    if new_status == 'aprovado':
        # Move para ApprovedCard e exclui da tabela original
        approved_card = ApprovedCard(**card.to_dict())
        db.session.add(approved_card)
        db.session.delete(card)

    db.session.commit()

