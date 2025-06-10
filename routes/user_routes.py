from flask import Blueprint, jsonify
from controllers import create_user, get_users, delete_user, login_user

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("test", methods=["GET"])
def test_route():
    return jsonify({"message": "Hello, world!"}), 200


user_bp.post("")(create_user)
user_bp.get("")(get_users)
user_bp.delete("/<int:user_id>")(delete_user)
user_bp.post("/login")(login_user)
