from flask import current_app


def get_supabase():
    """Retorna a instância do Supabase do app Flask"""
    return current_app.config.get("SUPABASE_CLIENT")
