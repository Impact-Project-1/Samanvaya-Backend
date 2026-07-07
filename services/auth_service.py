from repo import auth_repo
from schemas.auth import RegisterRequest, LoginRequest

def register(data: RegisterRequest) -> dict:
    return auth_repo.register_user(data)

def login(data: LoginRequest) -> dict:
    return auth_repo.login_user(data)
