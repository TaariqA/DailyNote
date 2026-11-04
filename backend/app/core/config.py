from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = "DailyNote"
    environment: str = "development"
    debug: bool = True

    database_url:str = Field(..., alias="DB_LINK")
    secret_key:str = Field(..., alias="JWT_SECRET_KEY")
    third_party_perfume_key:str = Field(..., alias="FRAGRANTYAI_KEY")
    jwt_algorithm = "HS256"
    access_token_expire_minutes = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )



settings = Settings()  #pyright:ignore[reportCallIssue]  #Values are loaded from environment variables.