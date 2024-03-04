
from flask import Blueprint, request, jsonify
from ..controllers.card_controller import create_card, get_cards, update_card_status
from ..services.pipefy_services import fetch_pipe_fields, fetch_card_fields

card_bp = Blueprint('api', __name__)

@card_bp.route('/cards', methods=['POST'])
def create_cards():
    data = request.get_json()
    return create_card(data)
def handle_get_cards():
    return get_cards()


@card_bp.route('/cards/<int:card_id>/status', methods=['PATCH'])

def change_card_status(card_id):
    data = request.get_json()
    new_status = data.get('status')

    if not new_status:
        return jsonify({'error': 'O status é obrigatório.'}), 400

    try:
        response = update_card_status(card_id, new_status)
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @card_bp.route("/pipe-fields/<pipe_id>", methods=["GET"])
# def get_pipe_fields(pipe_id):
#     # Fetch fields from Pipefy
#     fields = fetch_pipe_fields(pipe_id)
#
#     if fields is not None:
#         return jsonify(fields)
#     else:
#         return jsonify({"error": "Failed to fetch fields from Pipefy"}), 500
#
# @card_bp.route("/card-fields/<card_id>", methods=["GET"])
# def get_card_fields(card_id):
#     # Fetch field names from the specified card
#     field_names = fetch_card_fields(card_id)
#
#     if field_names is not None:
#         return jsonify(field_names)
#     else:
#         return jsonify({"error": "Failed to fetch card fields"}), 500