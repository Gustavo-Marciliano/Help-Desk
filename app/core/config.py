from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()

# BaseSettings: permite carregar configurações de variáveis de ambiente.
# DATABASE_URL: recebe a conexão do banco.
# env_file=".env": indica onde buscar as configurações.
# settings: disponibiliza essas configurações para o restante da aplicação.

# ---------------   