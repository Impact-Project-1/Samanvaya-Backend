from pydantic import BaseModel, EmailStr
from typing import Optional

class LoginRequest(BaseModel):
    username: str # email or phone
    password: str

class RegisterRequest(BaseModel):
    username: str # email or phone
    password: str
    confirm_password: str
    role: str # customer, vendor, admin

class AuthResponse(BaseModel):
    token: Optional[str] = None
    status_code: int
    error_message: Optional[str] = None
    success: bool
