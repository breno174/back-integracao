from flask import Blueprint
from controllers import create_zip, create_zip_for_user, delete_zip, generate_zip

zip_bp = Blueprint("zip", __name__, url_prefix="/zips")


zip_bp.post("")(create_zip)
zip_bp.get("/user/<int:user_id>")(create_zip_for_user)
zip_bp.delete("/<int:zip_id>")(delete_zip)
zip_bp.get("/generate/<int:user_id>")(generate_zip)
