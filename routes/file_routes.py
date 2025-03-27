from flask import Blueprint, request, jsonify
from models.files import File

file_bp = Blueprint("file", __name__, url_prefix="/files")


@file_bp.route(methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    file = request.files["file"]
    data = request.json
    if not data["user_id"]:
        return jsonify({"error": "Usuário não especificado"}), 400
    try:
        # file_record = save_file(user_id, file)
        response = File.upload_file(
            user_id=data["user_id"],
            file_name=data["file_name"],
            file_type=data["file_type"],
            zip_id=data.get("zip_id"),  # Opcional
        )
        return jsonify(response), 201
    except:
        return jsonify({"error": "Não foi possivel salvar o arquivo no banco"})


@file_bp.route("/user/<int:user_id>", methods=["GET"])
def get_files_by_user(user_id):
    files = File.get_files_by_user(user_id)
    return jsonify(files)


@file_bp.route("/zip/<int:zip_id>", methods=["GET"])
def get_files_by_zip(zip_id):
    files = File.get_files_by_zip(zip_id)
    return jsonify(files)


@file_bp.route("/<int:file_id>", methods=["DELETE"])
def delete_file(file_id):
    response = File.delete_file(file_id)
    return jsonify(response)
