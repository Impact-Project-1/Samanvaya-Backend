"""
Common configuration variables
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl, Annotated, Field
from supabase import create_client
from CONSTANTS import *

from supabase import Client


class Config(BaseSettings):
    # DB configurations
    SUPABASE_URL: str
    SUPABASE_KEY: str

    # middleware and network layer configurations
    ALLOW_ORIGINS: list[AnyHttpUrl] = []
    
    # storage configurations
    PROFILE_IMAGE_SIZE: Annotated[int, Field(default=FILESIZE_5MB, description="Value is in bytes, and the default value is 5MB, \
        This is the profile image size attributed to user(vendor and customer)")]
    VENDOR_IMAGE_SIZE: Annotated[int, Field(default=FILESIZE_MEDIUM, description="Vendor uploaded images of the business, \
        max file size")]
    
    model_config = SettingsConfigDict(env_file=".env.local")  # load the local env

    @property
    def supabase(self) -> Client:
        return create_client(self.SUPABASE_URL, self.SUPABASE_KEY)


# common instance indended for shared access
config = Config()

# export
__all__ = ["config"]
