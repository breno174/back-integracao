import os
import zipfile
from services.file_service import get_user_files
from models.zip import ZipFile

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "storage", "zips")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def create_zip_for_user(user_id, output_dir="zips"):
    """
    Cria um arquivo ZIP com todos os arquivos do usuário.
    """
    files = get_user_files(user_id)

    if not files:
        return None

    zip_filename = ZipFile.get_zips_by_user(user_id)[0]["zip_name"]
    if not zip_filename:
        raise ValueError("Linha de zip não encontrada no banco de dados.")
    zip_file_create = os.path.join(UPLOAD_FOLDER, f"zip_{user_id}_{zip_filename}.zip")

    with zipfile.ZipFile(zip_file_create, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            file_path = file["file_path"]

            if os.path.exists(file_path):
                zipf.write(file_path, os.path.basename(file_path))

    return zip_file_create


def get_existing_zip_for_user(user_id):
    """
    Retorna o caminho do ZIP existente para o usuário, se encontrado.
    Não gera o ZIP. Apenas retorna o caminho se o arquivo existir.
    """
    for filename in os.listdir(UPLOAD_FOLDER):
        if filename.startswith(f"zip_{user_id}_") and filename.endswith(".zip"):
            zip_path = os.path.join(UPLOAD_FOLDER, filename)
            return os.path.abspath(zip_path)

    return None


def delete_zip_service(user_id):
    """
    Deleta o arquivo ZIP especificado.
    """
    zip_path = get_zip_path(user_id=user_id)
    if not zip_path:
        print("Arquivo ZIP não encontrado no banco de dados.")
        return False
    if os.path.exists(zip_path):
        os.remove(zip_path)
        ZipFile.delete_zip(user_id)
        return True
    print("Arquivo ZIP não encontrado.")
    return False


def get_zip_path(user_id, output_dir="storage/zips"):
    """
    Retorna o caminho do arquivo ZIP do usuário.
    """
    zip_db = ZipFile.get_zips_by_user(user_id)
    if not zip_db:
        return None
    zip_filename = zip_db[0]["zip_name"]
    zip_path = os.path.join(UPLOAD_FOLDER, f"zip_{user_id}_{zip_filename}.zip")
    return zip_path if zip_filename else None


def get_zip_files(zip_path):
    """
    Retorna uma lista de arquivos contidos no arquivo ZIP.
    """
    if not os.path.exists(zip_path):
        return []

    with zipfile.ZipFile(zip_path, "r") as zipf:
        return zipf.namelist()


def extract_zip(zip_path, output_dir="extracted"):
    """
    Extrai o conteúdo do arquivo ZIP para o diretório especificado.
    """
    os.makedirs(output_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zipf:
        zipf.extractall(output_dir)

    return output_dir


def zip_file_exists(zip_path):
    """
    Verifica se o arquivo ZIP existe.
    """
    return os.path.exists(zip_path)


def get_zip_file_size(zip_path):
    """
    Retorna o tamanho do arquivo ZIP em bytes.
    """
    if os.path.exists(zip_path):
        return os.path.getsize(zip_path)
    return 0
