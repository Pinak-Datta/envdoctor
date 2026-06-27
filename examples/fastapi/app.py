from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    openai_api_key: str
    redis_url: str
    debug: bool = False


def create_app():
    settings = Settings()
    return {
        "database_url": settings.database_url,
        "openai_api_key": settings.openai_api_key,
        "redis_url": settings.redis_url,
        "debug": settings.debug,
    }
