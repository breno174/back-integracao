from flask import Blueprint, request, jsonify
from models.user import User

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route(methods=["POST"])
def create_user():
    data = request.json
    first_name = data.get("first_name")
    email = data.get("email")
    last_name = data.get("last_name")
    ip_address = data.get("ip_address")
    data_nascimento = data.get("data_nascimento")
    if not first_name or not email:
        return jsonify({"error": "Nome e email são obrigatórios"}), 400
    response = User.create_user(
        first_name, last_name, email, ip_address, data_nascimento
    )
    return jsonify(response), 201


@user_bp.route(methods=["GET"])
def get_users():
    users = User.get_users()
    return jsonify(users)


@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    response = User.delete_user(user_id)
    return jsonify(response)
