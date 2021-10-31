from pydantic import BaseModel


class AuthConfig(BaseModel):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


class BaseConfig:
    """Base configuration."""
    __SECRET_KEY = "fa688f3e53315727648fb7008d0ac87c3a15d95a2fa64ea4d4b92eb904802d84"
    __ALGORITHM = "HS256"
    __ACCESS_TOKEN_EXPIRE_MINUTES = 3000
    AUTH = AuthConfig(SECRET_KEY=__SECRET_KEY, ALGORITHM=__ALGORITHM,
                      ACCESS_TOKEN_EXPIRE_MINUTES=__ACCESS_TOKEN_EXPIRE_MINUTES)

    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
