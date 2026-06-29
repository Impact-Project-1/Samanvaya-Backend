from pydantic import Annotated, Field, EmailStr
from uuid import uuid4
from datetime import date
from schemas.base import RestrictedBase


class User(RestrictedBase):
    id: Annotated[
        uuid4, Field(default_factory=uuid4, description="user identification")
    ]
    name: Annotated[
        str, Field(..., max_length=50, min_length=3, description="Display name")
    ]
    email: Annotated[
        EmailStr, Field(..., description="email of the user")
    ]  # verify its not temp id

    phone: Annotated[
        str,
        Field(min_length=10, max_length=15)
    ]

    