import re
from flask import jsonify
from ..model.approved_cards import ApprovedCard
from ..model.card import Card
from .. import db


def is_email_valid(e_mail):
    # Regex simples para validação de e-mail
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, e_mail) is not None


def create_pipefy_cards(card_data):
    required_fields = [
        'tipo_de_pessoa', 'nome_raz_o_social', 'cpf', 'estado_civil',
        'telefone', 'e_mail', 'valor_total_da_compra', 'qual_tipo_de_im_vel',
        'cep', 'endere_o', 'n_mero', 'bairro', 'cidade', 'estado',
        'qual_valor_do_im_vel', 'qual_o_valor_do_empr_stimo',
        'prazo_pagamento',
    ]

    missing_fields = [field for field in required_fields if not card_data.get(field)]
    if missing_fields:
        return jsonify({'message': 'Campos obrigatórios estão faltando: ' + ', '.join(missing_fields)}), 400

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
        status=card_data.get('status')
    )
    db.session.add(new_card)
    db.session.commit()

    # cria cards no pipefy
    # data = create_pipefy_card(card_data)

    return jsonify({'message': 'Card criado com sucesso', 'card': new_card.to_dict()}), 201


def get_cards():
    cards = Card.query.all()
    cards_list = [card.to_dict() for card in cards]
    return jsonify(cards_list), 200


def get_card_by_id(card_id):
    card = Card.query.get(card_id)
    # Verifica se o card foi encontrado
    if card is not None:
        # Card encontrado, retorna os dados do card
        return jsonify(card.to_dict()), 200
    else:
        # Card não encontrado, retorna uma mensagem de erro
        return jsonify({'message': 'Card não encontrado.'}), 404


def approve_cards():
    # Busca todos os cards aprovados atuais
    current_approved_cards = ApprovedCard.query.all()
    current_approved_cards_list = [card.to_dict() for card in current_approved_cards]

    # Define cards_to_approve antes dos blocos condicionais para garantir que sempre tenha um valor definido
    cards_to_approve = Card.query.filter_by(status='Aprovado').all()

    if not current_approved_cards and not cards_to_approve:
        # Caso não existam cards aprovados atualmente nem cards para aprovar
        return jsonify({
                           'message': 'Nenhum card aprovado atualmente na tabela ApprovedCard e nenhum card com status Aprovado para mover.',
                           'approved_cards': []}), 200

    for card in cards_to_approve:
        approved_card_data = card.to_dict()
        # Assegura-se de remover 'id' para evitar conflitos
        approved_card_data.pop('id', None)
        approved_card = ApprovedCard(**approved_card_data)
        db.session.add(approved_card)
        db.session.delete(card)

    db.session.commit()

    # Atualiza a lista de cards aprovados após mover os novos
    updated_approved_cards = ApprovedCard.query.all()
    updated_approved_cards_list = [card.to_dict() for card in updated_approved_cards]

    return jsonify({
        'message': f'{len(cards_to_approve)} cards movidos para aprovados com sucesso, se houver.',
        'approved_cards': updated_approved_cards_list
    }), 200


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
