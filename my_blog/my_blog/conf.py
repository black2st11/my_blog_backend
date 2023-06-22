from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str
    TEST_DB_URL: str
    SECRET_KEY: str
    DEBUG: bool
    DB_ENGINE: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: str
    DB_HOST: str
    CORS_ORIGIN_WHITELIST: list[AnyHttpUrl | str]
    ALLOWED_HOSTS: list[AnyHttpUrl | str]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
