
from flask import Blueprint, jsonify
from ..controllers.card_controller import create_card
from ..services.pipefy_services import fetch_pipe_fields, fetch_card_fields

card_bp = Blueprint('api', __name__)

@card_bp.route('/cards', methods=['POST'])
def create():
    return create_card()
@card_bp.route("/pipe-fields/<pipe_id>", methods=["GET"])
def get_pipe_fields(pipe_id):
    # Fetch fields from Pipefy
    fields = fetch_pipe_fields(pipe_id)

    if fields is not None:
        return jsonify(fields)
    else:
        return jsonify({"error": "Failed to fetch fields from Pipefy"}), 500

@card_bp.route("/card-fields/<card_id>", methods=["GET"])
def get_card_fields(card_id):
    # Fetch field names from the specified card
    field_names = fetch_card_fields(card_id)

    if field_names is not None:
        return jsonify(field_names)
    else:
        return jsonify({"error": "Failed to fetch card fields"}), 500