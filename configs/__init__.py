from flask import Flask
from dotenv import load_dotenv
from os import getenv
from supabase import create_client
from dotenv import find_dotenv

find_dotenv()
# Load environment variables from .env file
load_dotenv()


def init_app(app: Flask):
    url = f"https://" + getenv("SUPABASE_URL")
    SUPABASE_URL = url
    SUPABASE_KEY = getenv("SUPABASE_KEY")
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError(
            "As variáveis SUPABASE_URL e SUPABASE_SERVICE_KEY precisam estar definidas."
        )
    try:
        print("Criando cliente Supabase...")
        print(f"URL: {SUPABASE_URL}")
        print("...\b\f\f\f")
        app.config["SUPABASE_CLIENT"] = create_client(SUPABASE_URL, SUPABASE_KEY)
    except Exception as e:
        raise ValueError(f"Erro ao criar o cliente Supabase: {e}")
