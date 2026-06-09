# repo/category_repo.py

from config import config

client = config.supabase

def get_categories() -> list[dict]:
    response = (
        client
        .table("categories")
        .select("*")
        .order("name")
        .execute()
    )

    return response.data
