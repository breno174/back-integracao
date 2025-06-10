from flask import request, jsonify
from models.user import User

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


def get_users():
    try:
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)

        users = User.get_users(page=page, per_page=per_page)

        return jsonify(users), 200

    except Exception as e:
        return jsonify({"error": f"Erro ao buscar usuários: {str(e)}"}), 500


def delete_user(user_id):
    response = User.delete_user(user_id)
    return jsonify(response)

def login_user():
    data = request.json
    email = data.get("email")
    ip_address = data.get("ip_address")

    if not email or not ip_address:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    try:
        user = User.login(email, ip_address)
        if user:
            return jsonify({"message": "Login bem-sucedido", "user": user}), 200
        else:
            return jsonify({"error": "Email ou senha incorretos"}), 401
    except Exception as e:
        return jsonify({"error": f"Erro ao fazer login: {str(e)}"}), 500