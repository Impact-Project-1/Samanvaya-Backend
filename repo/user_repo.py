"""Handle operations related to user authetication and authorization, 
the user attributes like verfied and active (and others) are stored as user_metadata
in the auth.users table in Supabase.

"""

from config import config
from schemas.user import UserRegistration, User, UserLogin

client = config.supabase

def create_user(user: UserRegistration) -> dict:
    auth_response = (
        client
        .auth
        .sign_up({
            "email": user.email,
            "password": user.password,
            "options":{
                "user_metadata":{
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone_number": user.phone_number,
                }
            }
        })
    )

    user_data = ({
        "id": auth_response.user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone_number": user.phone_number,
        "verified": False
    })

    response = (
        client
        .table("users")
        .insert(user_data)
        .execute()
    )

    return {
        "message": "User created successfully",
        "token": auth_response.session.access_token,
        "user_data": {
            "id": auth_response.user.id,
            "first_name": auth_response.user.user_metadata.first_name,
            "last_name": auth_response.user.user_metadata.last_name,
            "email": auth_response.user.email,
            "phone_number": auth_response.user.user_metadata.phone_number,
            "verified": auth_response.user.user_metadata.verified
        }
    }

def login_user(user: UserLogin) -> dict:
    response = (
        client
        .auth
        .sign_in_with_password({
            "email": user.email,
            "password": user.password,
        })
    )
    return {
        "message": "User logged in successfully",
        "token": response.session.access_token,
        "user_data": {
            "id": response.user.id,
            "first_name": response.user.user_metadata.first_name,
            "last_name": response.user.user_metadata.last_name,
            "email": response.user.email,
            "phone_number": response.user.user_metadata.phone_number,
            "verified": response.user.user_metadata.verified
        }
    }

def get_user(id: str) -> dict:
    response = (
        client
        .table("users")
        .select("*")
        .eq("id", id)
        .execute()
    )
    return User(**response.data[0])
