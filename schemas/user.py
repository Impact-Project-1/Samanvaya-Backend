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

    created_at: Annotated[
        date,
        Field(
            default_factory=date.today,
            description="date at which the corresponding record was created",
        ),
    ]
    updated_at: Annotated[
        date,
        Field(
            default_factory=date.today,
            description="date at which an update was meade on the record",
        ),
    ]
