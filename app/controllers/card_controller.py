import re

from flask import jsonify, request

from ..model.approved_cards import ApprovedCard
from ..services.pipefy_services import create_pipefy_card
from ..model.card import Card
from .. import db


def is_email_valid(e_mail):
    # Regex simples para validação de e-mail
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, e_mail) is not None


def create_pipefy_cards(card_data):

    new_card = Card(
        tipo_de_pessoa=card_data.get('tipo_de_pessoa'),
        nome_raz_o_social=card_data.get('nome_raz_o_social'),
        cpf=card_data.get('cpf'),
        estado_civil=card_data.get('estado_civil'),
        telefone=card_data.get('telefone'),
        e_mail=card_data.get('e_mail'),
        valor_total_da_compra=card_data.get('valor_total_da_compra'),
        qual_tipo_de_im_vel=card_data.get('qual_tipo_de_im_vel'),
        cep=card_data.get('cep'),
        endere_o=card_data.get('endere_o'),
        n_mero=card_data.get('n_mero'),
        bairro=card_data.get('bairro'),
        cidade=card_data.get('cidade'),
        estado=card_data.get('estado'),
        qual_valor_do_im_vel=card_data.get('qual_valor_do_im_vel'),
        qual_o_valor_do_empr_stimo=card_data.get('qual_o_valor_do_empr_stimo'),
        prazo_pagamento=card_data.get('prazo_pagamento'),
        indica_o=card_data.get('indica_o'),
        assessor_respons_vel=card_data.get('assessor_respons_vel'),
    )
    db.session.add(new_card)
    db.session.commit()

    data = create_pipefy_card(card_data)

    return jsonify({'message': 'Card criado com sucesso', 'card': new_card.to_dict()}, data), 201


def create_card(data):

    # Salva card no banco de dados
    new_card = Card(
        tipo_de_pessoa=data.get('tipo_de_pessoa'),
        nome_raz_o_social=data.get('nome_raz_o_social'),
        cpf=data.get('cpf'),
        estado_civil=data.get('estado_civil'),
        telefone=data.get('telefone'),
        e_mail=data.get('email'),
        valor_total_da_compra=data.get('valor_total_da_compra'),
        qual_tipo_de_im_vel=data.get('qual_tipo_de_im_vel'),
        cep=data.get('cep'),
        endere_o=data.get('endere_o'),
        n_mero=data.get('n_mero'),
        bairro=data.get('bairro'),
        cidade=data.get('cidade'),
        estado=data.get('estado'),
        qual_valor_do_im_vel=data.get('qual_valor_do_im_vel'),
        qual_o_valor_do_empr_stimo=data.get('qual_o_valor_do_empr_stimo'),
        prazo_para_pagamento=data.get('prazo_para_pagamento'),
        indica_o=data.get('indica_o'),
        assessor_respons_vel=data.get('301990243'),
        pol_tica_de_privacidade=data.get('Li e concordo com a Política e Privacidade'),
    )
    db.session.add(new_card)
    db.session.commit()

    return jsonify({'message': 'Card criado com sucesso', 'card': new_card.to_dict()}, card_data), 201


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
