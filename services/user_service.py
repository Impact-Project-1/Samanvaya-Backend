from config import config
from repo import user_repo
from schemas.user import User, UserRegistration, UserLogin

def create_user(user: UserRegistration) -> User:
    """Return the User object if the registration was successful"""
    response = user_repo.create_user(user)
    return User(
        id=response["user_data"]["id"],
        first_name=response["user_data"]["first_name"],
        last_name=response["user_data"]["last_name"],
        email=response["user_data"]["email"],
        phone_number=response["user_data"]["phone_number"],
        verified=response["user_data"]["verified"]
    )

def login_user(user: UserLogin) -> User:
    """Return the User object if the login was successful"""
    response = user_repo.login_user(user)
    return User(
        id=response["user_data"]["id"],
        first_name=response["user_data"]["first_name"],
        last_name=response["user_data"]["last_name"],
        email=response["user_data"]["email"],
        phone_number=response["user_data"]["phone_number"],
        verified=response["user_data"]["verified"]
    )

def get_user(id: str) -> User:
    """Return the User object if the user was found"""
    response = user_repo.get_user(id)
    return User(
        id=response["id"],
        first_name=response["first_name"],
        last_name=response["last_name"],
        email=response["email"],
        phone_number=response["phone_number"],
        verified=response["verified"]
    )