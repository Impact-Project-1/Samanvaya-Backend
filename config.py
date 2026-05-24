"""
Common configuration variables
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from supabase import create_client

from supabase import Client


class Config(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_KEY: str

    model_config = SettingsConfigDict(env_file=".env.local")  # load the local env

    @property
    def supabase(self) -> Client:
        return create_client(self.SUPABASE_URL, self.SUPABASE_KEY)


# common instance indended for shared access
config = Config()

# export
__all__ = ["config"]
