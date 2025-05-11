from flask import request, jsonify
from models.zip import ZipFile
from services.zip_service import (
    create_zip_for_user,
    delete_zip_service,
    get_existing_zip_for_user,
)
import os
from flask import send_file


def create_zip_controller():
    data = request.json
    response = ZipFile.create_zip_in_db(data["user_id"], data["zip_name"])
    return jsonify(response), 201


def get_zips_by_user(user_id):
    zips = ZipFile.get_zips_by_user(user_id)
    return jsonify(zips)


def delete_zip(user_id):
    response = delete_zip_service(user_id)
    if response == False:
        return (
            jsonify(
                {
                    "error": "Arquivo ZIP não encontrado ou zip não salvo no banco de dados."
                }
            ),
            404,
        )
    return jsonify(response), 201


def generate_zip(user_id):
    """
    Gera um ZIP com os arquivos do usuário e retorna o caminho.
    """
    zip_path = create_zip_for_user(user_id)

    if not zip_path:
        return jsonify({"error": "Nenhum arquivo encontrado para o usuário"}), 404

    return jsonify({"zip_path": zip_path}), 200


def download_zip(user_id):
    try:
        zip_path = get_existing_zip_for_user(user_id)

        if not zip_path:
            return (
                jsonify({"error": "Arquivo ZIP não encontrado para este usuário"}),
                404,
            )

        return send_file(
            zip_path, as_attachment=True, download_name=os.path.basename(zip_path)
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500
