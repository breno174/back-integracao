from models import get_supabase

UPLOAD_FOLDER = "storage/files"


class File:
    @staticmethod
    def upload_file(user_id, file_name, file_type, zip_id=None):
        supabase = get_supabase()
        data = {
            "user_id": user_id,
            "file_name": file_name,
            "file_type": file_type,
            "zip_id": zip_id,
            "file_path": UPLOAD_FOLDER,
        }
        response = supabase.table("files").insert(data).execute()
        return response

    @staticmethod
    def get_files_by_user(user_id):
        supabase = get_supabase()
        response = supabase.table("files").select("*").eq("user_id", user_id).execute()
        return response.data

    @staticmethod
    def get_files_by_zip(zip_id):
        supabase = get_supabase()
        response = supabase.table("files").select("*").eq("zip_id", zip_id).execute()
        return response.data

    @staticmethod
    def delete_file(file_id):
        supabase = get_supabase()
        response = supabase.table("files").delete().eq("id", file_id).execute()
        return response
