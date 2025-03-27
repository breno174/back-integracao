from flask import request, jsonify
from models.files import File
from services.file_service import save_file


def upload_files():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files["file"]
    data = request.json

    if not data.get("user_id"):
        return jsonify({"error": "Usuário não especificado"}), 400

    try:
        # Salva o arquivo e registra no banco
        file_record = save_file(data["user_id"], file)
        return jsonify(file_record), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao salvar o arquivo: {str(e)}"}), 500


def get_files_by_user(user_id):
    try:
        files = File.get_files_by_user(user_id)
        return jsonify(files), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar arquivos: {str(e)}"}), 500


def get_files_by_zip(zip_id):
    files = File.get_files_by_zip(zip_id)
    return jsonify(files)


def delete_file(file_id):
    response = File.delete_file(file_id)
    return jsonify(response)
