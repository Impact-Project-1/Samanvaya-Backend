from fastapi import APIRouter
from services import category_service

router = APIRouter(prefix="/api/v1/categories", tags=["Categories"])

@router.get("/")
def get_categories():
    return category_service.get_categories()