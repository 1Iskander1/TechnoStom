from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_url: str = "mysql+aiomysql://root:123456789@localhost/demofayzulloev222"
    # db_url: str = "mysql+aiosmysql:///./db.sqlite3"
    db_echo: bool = True


# f"mysql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_PORT}/{self.DB_NAME}"
settings = Setting()
