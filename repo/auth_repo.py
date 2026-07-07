from config import config
from schemas.auth import RegisterRequest, LoginRequest
import logging

client = config.supabase

def register_user(data: RegisterRequest) -> dict:
    try:
        # Supabase auth signup
        auth_response = client.auth.sign_up({
            "email": data.username if "@" in data.username else f"{data.username}@temp.com",
            "password": data.password,
            "options": {
                "user_metadata": {
                    "role": data.role,
                    "verified": False,
                }
            }
        })
        
        user_id = auth_response.user.id
        
        # Insert into specific table based on role
        if data.role == "customer":
            client.table("customers").insert({"id": user_id}).execute()
        elif data.role == "vendor":
            client.table("vendors").insert({"vendor_id": user_id}).execute()

        return {
            "success": True,
            "status_code": 201,
            "token": auth_response.session.access_token if auth_response.session else None,
            "error_message": None
        }
    except Exception as e:
        logging.error(f"Error registering user: {e}")
        return {
            "success": False,
            "status_code": 400,
            "token": None,
            "error_message": str(e)
        }

def login_user(data: LoginRequest) -> dict:
    try:
        auth_response = client.auth.sign_in_with_password({
            "email": data.username if "@" in data.username else f"{data.username}@temp.com",
            "password": data.password,
        })
        return {
            "success": True,
            "status_code": 200,
            "token": auth_response.session.access_token,
            "error_message": None
        }
    except Exception as e:
        logging.error(f"Error logging in user: {e}")
        return {
            "success": False,
            "status_code": 401,
            "token": None,
            "error_message": str(e)
        }
