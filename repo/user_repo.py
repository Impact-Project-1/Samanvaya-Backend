"""Handle operations related to user authetication and authorization, 
the user attributes like verfied and active (and others) are stored as user_metadata
in the auth.users table in Supabase.

"""

from config import config
from schemas.user import UserRegistration, User, UserLogin

client = config.supabase

def create_user(user:UserRegistration) -> dict:
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
                    "phone_number": user.phone,
                }
            }
        })
    )

    user_data = ({
        "id": auth_response.user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone_number": user.phone,
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
        "token": auth_response.session.access_token
    }

def login_user(user:UserLogin) -> dict:
    response = (
        client
        .table("users")
        .select("*")
        .eq("email", user.email)
        .execute()
    )
    return response.data

def get_user(id:str) -> dict:
    response = (
        client
        .table("users")
        .select("*")
        .eq("id", id)
        .execute()
    )
    return User(**response.data[0])
