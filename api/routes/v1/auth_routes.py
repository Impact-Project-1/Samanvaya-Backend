from fastapi import APIRouter, HTTPException, status
from schemas.auth import RegisterRequest, LoginRequest, AuthResponse
from services import auth_service

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=AuthResponse)
def register(data: RegisterRequest):
    result = auth_service.register(data)
    if not result["success"]:
        raise HTTPException(status_code=result["status_code"], detail=result["error_message"])
    return result

@router.post("/login", response_model=AuthResponse)
def login(data: LoginRequest):
    result = auth_service.login(data)
    if not result["success"]:
        raise HTTPException(status_code=result["status_code"], detail=result["error_message"])
    return result
