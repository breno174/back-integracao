import os
from werkzeug.utils import secure_filename
from models.files import File

# Defina o diretório onde os arquivos serão armazenados no servidor
UPLOAD_FOLDER = "storage/files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Cria a pasta se ela não existir


def save_file(user_id, file):
    """
    Processa o upload de um arquivo e registra no banco de dados.
    """
    # Garante que o nome do arquivo seja seguro
    filename = secure_filename(file.filename)

    # Gera o caminho completo onde o arquivo será salvo
    file_path = os.path.join(UPLOAD_FOLDER, f"user_{user_id}_{filename}")

    # Salva o arquivo fisicamente no servidor
    file.save(file_path)

    # Agora, insere o arquivo no banco de dados com o caminho correto
    file_record = File.create_file(user_id, filename, file.mimetype, file_path)

    return file_record
