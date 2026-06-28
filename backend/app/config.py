from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Offline Invoice Intelligence System"
    database_url: str = "sqlite:///./data/invoices.db"
    upload_dir: Path = Path("data/uploads")
    llama_cpp_bin: Path | None = None
    tinyllama_gguf_path: Path | None = None
    llama_timeout_seconds: int = 45
    demo_mode: bool = True

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
