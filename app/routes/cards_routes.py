
from flask import Blueprint
from ..controllers.card_controller import create_card

card_bp = Blueprint('card', __name__)

@card_bp.route('/cards', methods=['POST'])
def create():
    return create_card()
