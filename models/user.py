from models import get_supabase


class User:
    @staticmethod
    def create_user(first_name, last_name, email, ip_address, data_nascimento):
        supabase = get_supabase()
        data = {
            "first_name": first_name,
            "email": email,
            "last_name": last_name,
            "ip_address": ip_address,
            "data_nascimento": data_nascimento,
        }
        response = supabase.table("person").insert(data).execute()
        return response.data

    @staticmethod
    def get_users(page=1, per_page=10):
        supabase = get_supabase()
        offset = (page - 1) * per_page

        response = (
            supabase.table("person")
            .select("*")
            .range(offset, offset + per_page - 1)
            .execute()
        )
        return response.data

    @staticmethod
    def get_user_by_id(user_id):
        supabase = get_supabase()
        response = supabase.table("person").select("*").eq("id", user_id).execute()
        return response.data

    @staticmethod
    def delete_user(user_id):
        supabase = get_supabase()
        response = supabase.table("person").delete().eq("id", user_id).execute()
        return response.data
