import re

from datetime import date
from pydantic import Annotated, Field, EmailStr, model_validator, AfterValidator, ConfigDict
from typing import Self
from uuid import uuid4

from core.validate import validate_password_strength, validate_phone_number
from schemas.base import RestrictedBase, Base

class User(RestrictedBase):
    """user's identity within the system is handled internally through ids of type uuid,
    user data circulated within the system at the application layer"""

    first_name: Annotated[str, Field(..., max_length=50, min_length=3, description="Display name")]
    last_name: Annotated[str, Field(default="", description="Last name is optional")]
    email: Annotated[EmailStr, Field(..., description="email of the user")]
    phone_number: Annotated[str,Field(min_length=10, max_length=15)]
    verified: Annotated[bool,Field(default=False, description="Flag to mark whether the user is verfied or not")]

    model_config = ConfigDict(
        extra='ignore',
        str_strip_whitespace=True,
    )

class UserRegistration(Base):
    """User registration scheme"""

    first_name: Annotated[str, Field(..., min_length=2, max_length=50)]
    last_name: Annotated[str, Field(default="", description="Last name is optional")]
    email: Annotated[EmailStr, Field(..., description="Email id of the user")]
    phone_number: Annotated[str, Field(..., examples=["+91 8089033138"]), AfterValidator(validate_phone_number)]
    
    password: Annotated[str, Field(..., description="Secure password in plaintext"), AfterValidator(validate_password_strength)]
    cnf_password: Annotated[str, Field(..., description="Secure password repeat, for server side validation")]

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.password != self.cnf_password:
            raise ValueError("Passwords do not match")
        return self


class UserLogin(Base):
    """User Login scheme"""

    email: Annotated[EmailStr, Field(..., description="Email of the user")]
    password: Annotated[str, Field(...)]


class PasswordUpdate(Base):

    current_password: Annotated[str, Field(..., description="Current password")]
    password: Annotated[str, Field(..., description="New password"), AfterValidator(validate_password_strength)]
    cnf_password: Annotated[str, Field(..., description="New password repeat, for server side validation")]

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        if self.password != self.cnf_password:
            raise ValueError("Passwords do not match")
        return self