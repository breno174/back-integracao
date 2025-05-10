import os
import zipfile
from services.file_service import get_user_files


def create_zip_for_user(user_id, output_dir="zips"):
    """
    Cria um arquivo ZIP com todos os arquivos do usuário.
    """
    files = get_user_files(user_id)

    if not files:
        return None

    os.makedirs(output_dir, exist_ok=True)

    zip_filename = os.path.join(output_dir, f"user_{user_id}.zip")

    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            file_path = file["file_path"]

            if os.path.exists(file_path):
                zipf.write(file_path, os.path.basename(file_path))

    return zip_filename
