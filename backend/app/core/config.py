from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):

    PROJECT_NAME: str = "FastAPI Template"
    PROJECT_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"

    POSTGRES_USER: str = Field(default=...)
    POSTGRES_PASSWORD: str = Field(default=...)
    POSTGRES_HOST: str = Field(default=...)
    POSTGRES_PORT: str = Field(default=...)
    POSTGRES_DB: str = Field(default=...)

    @property
    def POSTGRES_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()