from pydantic import Annotated, ConfigDict, Field
from schemas.base import RestrictedBase


class User(RestrictedBase):
    id: Annotated[str, Field()]
