from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    BITGET_KEY: str
    BITGET_SECRET: str
    BITGET_PASS: str

    OKX_KEY: str
    OKX_SECRET: str
    OKX_PASS: str


config = Settings()
