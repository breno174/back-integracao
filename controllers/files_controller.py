from flask import request, jsonify
from models.files import File
from services.file_service import save_file, get_user_files


def upload_files():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files["file"]
    data = request.form.to_dict(flat=False)
    print("file.mimetype", file.mimetype)
    print("file.filename", file.filename)
    if not data.get("user_id"):
        return jsonify({"error": "Usuário não especificado"}), 400

    try:
        # Salva o arquivo e registra no banco
        file_record = save_file(data["user_id"], file)
        return jsonify(file_record), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao salvar o arquivo: {str(e)}"}), 400


def get_files_db_by_user(user_id):
    if not user_id:
        return jsonify({"error": "Usuário não especificado"}), 400
    try:
        files = get_user_files(user_id)
        return jsonify(files), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar arquivos: {str(e)}"}), 500


def get_files_by_zip(zip_id):
    files = File.get_files_by_zip(zip_id)
    return jsonify(files)


def delete_file(file_id):
    response = File.delete_file(file_id)
    return jsonify(response)
