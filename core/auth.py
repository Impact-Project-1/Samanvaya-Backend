from fastapi import Header, HTTPException
from config import config

supabase = config.supabase

def get_current_user(
    authorization: str | None = Header(default=None)
):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Missing Authorization header"
        )

    token = authorization.replace("Bearer ", "")

    user_response = supabase.auth.get_user(token)

    if not user_response.user:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return user_response.user