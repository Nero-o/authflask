
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin, CORS

from ..controllers.card_controller import get_cards, update_card_status, create_pipefy_cards, approve_cards

card_bp = Blueprint('api', __name__)
CORS(card_bp)


@card_bp.route('/pipefy', methods=['POST'])
def create_pipefy():
    data = request.get_json()
    return create_pipefy_cards(data)


@card_bp.route('/pipefy/get_cards', methods=['GET'])
def handle_get_cards():
    return get_cards()


@card_bp.route('/pipefy/approve_cards', methods=['POST'])
def handle_approve_cards():
    return approve_cards()


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