import logging
from os import environ
from typing import Any, Self, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8", env_nested_delimiter="__", extra="ignore")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        logger.debug(f"Config initialized: {self.model_dump()}")

    @classmethod
    def from_env(cls) -> Self:
        return cls(
            _env_file=environ.get("ENV_FILE", ".env"),
            _secrets_dir=environ.get("SECRETS_DIR"),
        )


class DatabaseConfig(BaseSettings):
    url: str = Field(default="postgresql://localhost/defaultdb", description="Database connection URL")

    model_config = SettingsConfigDict(env_prefix="DATABASE__", env_nested_delimiter="__")


class RedisConfig(BaseSettings):
    url: str = Field(default="redis://localhost:6379/0", description="Redis connection URL")

    model_config = SettingsConfigDict(env_prefix="REDIS__", env_nested_delimiter="__")


class ServicesConfig(BaseSettings):
    exam_url: Optional[str] = Field(default="http://localhost:8000/exams", description="Exam service URL")

    model_config = SettingsConfigDict(env_prefix="SERVICES__", env_nested_delimiter="__")


class AppConfig(BaseConfig):
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    redis: RedisConfig = Field(default_factory=RedisConfig)
    services: ServicesConfig = Field(default_factory=ServicesConfig)

    @classmethod
    def from_env(cls) -> Self:
        try:
            config = super().from_env()

            # Validate critical configurations
            if not config.database.url:
                raise ValueError("Database URL is required")

            if not config.redis.url:
                raise ValueError("Redis URL is required")

            logger.info("Configuration loaded successfully")
            return config

        except Exception as e:
            logger.error(f"Failed to load configuration: {e}")

            # Provide fallback configuration with defaults
            fallback_config = cls(database=DatabaseConfig(), redis=RedisConfig(), services=ServicesConfig())

            logger.warning("Using fallback configuration")
            return fallback_config

    def validate_config(self):
        """
        Additional custom validation method
        """
        errors = []

        if not self.database.url.startswith(("postgresql://", "postgres://")):
            errors.append("Invalid database URL format")

        if not self.redis.url.startswith("redis://"):
            errors.append("Invalid Redis URL format")

        if errors:
            raise ValueError(f"Configuration validation errors: {', '.join(errors)}")

        return self


def load_config() -> AppConfig:
    """
    Centralized configuration loading function
    """
    try:
        config = AppConfig.from_env()
        return config.validate_config()
    except Exception as e:
        logger.error(f"Critical configuration error: {e}")
        raise
