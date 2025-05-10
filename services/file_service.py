import os
from werkzeug.utils import secure_filename
from models.files import File
from models.zip import ZipFile
from models import get_supabase

# Defina o diretório onde os arquivos serão armazenados no servidor
UPLOAD_FOLDER = "storage/files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Cria a pasta se ela não existir


def save_file(user_id, file):
    """
    Processa o upload de um arquivo e registra no banco de dados.
    """
    # Garante que o nome do arquivo seja seguro
    filename = secure_filename(file.filename)
    if isinstance(user_id, list):
        user_id = user_id[0]
    user_id = int(user_id)

    # Gera o caminho completo onde o arquivo será salvo
    file_path = os.path.join(UPLOAD_FOLDER, f"user_{user_id}_{filename}")

    # Salva o arquivo fisicamente no servidor
    file.save(file_path)
    zip_file = ZipFile.get_zips_by_user(user_id)
    if zip_file:
        user_id_zip = zip_file[0]["user_id"]
        if user_id_zip != user_id:
            raise ValueError(
                "O usuário não tem permissão para acessar este arquivo zip."
            )
        else:
            zip_id = zip_file[0]["id"]
    else:
        zip_id = None
    # Verifica se o arquivo já existe no banco de dados
    existing_file = File.get_files_db_by_user(user_id)
    if existing_file:
        for existing in existing_file:
            if existing["file_name"] == filename and existing["zip_id"] == zip_id:
                raise ValueError("Arquivo já existe no banco de dados.")

    file_record = File.upload_file(user_id, filename, file.mimetype, file_path, zip_id)

    return file_record


def get_user_files(user_id):
    """
    Busca todos os arquivos vinculados a um usuário no Supabase.
    """
    supabase = get_supabase()
    response = supabase.table("files").select("*").eq("user_id", user_id).execute()

    if not response.data:
        return []

    return response.data
