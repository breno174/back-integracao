from flask import Blueprint
from controllers import upload_files, get_files_by_user, get_files_by_zip, delete_file

file_bp = Blueprint("file", __name__, url_prefix="/files")

file_bp.post("")(upload_files)
file_bp.get("/user/<int:user_id>")(get_files_by_user)
file_bp.get("/zip/<int:zip_id>")(get_files_by_zip)
file_bp.delete("/<int:file_id>")(delete_file)
