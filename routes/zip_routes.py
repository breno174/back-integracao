from flask import Blueprint
from controllers import (
    create_zip_controller,
    delete_zip,
    generate_zip,
    get_zips_by_user,
)

zip_bp = Blueprint("zip", __name__, url_prefix="/zips")


zip_bp.post("")(create_zip_controller)
zip_bp.get("/user/<int:user_id>")(get_zips_by_user)
zip_bp.delete("/<int:zip_id>")(delete_zip)
zip_bp.get("/generate/<int:user_id>")(generate_zip)
