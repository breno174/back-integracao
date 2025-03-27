from flask import Flask
from dotenv import load_dotenv
from os import getenv
from supabase import create_client

load_dotenv()


def init_app(app: Flask):
    SUPABASE_URL = getenv("SUPABASE_URL")
    SUPABASE_KEY = getenv("SUPABASE_KEY")
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError(
            "As variáveis SUPABASE_URL e SUPABASE_SERVICE_KEY precisam estar definidas."
        )

    app.config["SUPABASE_CLIENT"] = create_client(SUPABASE_URL, SUPABASE_KEY)
