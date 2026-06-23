# services/category_service.py

from repo import category_repo

def get_categories() -> list[dict]:
    return category_repo.get_categories()