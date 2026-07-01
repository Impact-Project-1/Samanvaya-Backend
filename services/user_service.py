from config import config
from repo import user_repo
from schemas.user import User, UserRegistration, UserLogin

def create_user(user:UserRegistration) -> dict:
    return user_repo.create_user(user)

def login_user(user:UserLogin) -> dict:
    return user_repo.login_user(user)

