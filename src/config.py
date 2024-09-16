from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App settings"""

    SECRET_KEY: str = "default_secret_key"
    DB_URL: str = "sqlite+aiosqlite:///database.sqlite3"

    class Config:
        """Settings config"""

        env_file = ".env"


@lru_cache(maxsize=1, typed=True)
def get_settings() -> Settings:
    """Get an instance of Settings class"""
    return Settings()
