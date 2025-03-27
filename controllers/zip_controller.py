from flask import request, jsonify
from models.zip import ZipFile
from services.zip_service import create_zip_for_user


def create_zip():
    data = request.json
    response = ZipFile.create_zip(data["user_id"], data["zip_name"])
    return jsonify(response), 201


def get_zips_by_user(user_id):
    zips = ZipFile.get_zips_by_user(user_id)
    return jsonify(zips)


def delete_zip(zip_id):
    response = ZipFile.delete_zip(zip_id)
    return jsonify(response)


def generate_zip(user_id):
    """
    Gera um ZIP com os arquivos do usuário e retorna o caminho.
    """
    zip_path = create_zip_for_user(user_id)

    if not zip_path:
        return jsonify({"error": "Nenhum arquivo encontrado para o usuário"}), 404

    return jsonify({"zip_path": zip_path}), 200
