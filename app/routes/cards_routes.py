from flask import Blueprint, request
from flask_cors import CORS

from ..controllers.card_controller import get_cards, create_pipefy_cards, approve_cards, get_card_by_id

card_bp = Blueprint('api', __name__)
CORS(card_bp)


@card_bp.route('/pipefy', methods=['POST'])
def create_pipefy():
    data = request.get_json()
    return create_pipefy_cards(data)


@card_bp.route('/pipefy/get_cards', methods=['GET'])
def handle_get_cards():
    return get_cards()


@card_bp.route('/cards/<int:card_id>', methods=['GET'])
def handle_get_card_by_id(card_id):
    return get_card_by_id(card_id)

@card_bp.route('/pipefy/approve_cards', methods=['POST'])
def handle_approve_cards():
    return approve_cards()
