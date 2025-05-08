from models import get_supabase


class ZipFile:
    @staticmethod
    def create_zip(user_id, zip_name):
        supabase = get_supabase()
        data = {"user_id": user_id, "zip_name": zip_name}
        response = supabase.table("zips").insert(data).execute()
        return response.data

    @staticmethod
    def get_zips_by_user(user_id):
        supabase = get_supabase()
        response = supabase.table("zips").select("*").eq("user_id", user_id).execute()
        return response.data

    @staticmethod
    def delete_zip(zip_id):
        supabase = get_supabase()
        response = supabase.table("zips").delete().eq("id", zip_id).execute()
        return response.data
