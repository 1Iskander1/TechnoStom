from pydantic_settings import BaseSettings


class Valid:
    def __init__(self):
        self.count = 0

    def bool_false(self):
        return False

    def bool_true(self):
        return True

    def count1(self):
        self.count += 1
        c = self.count
        return c


# DB_LOGIN = ""
# DB_NAME = ""
# r = Valid()
# if r.count1() == 1:
#     bf = r.bool_false()
# else:
#     bf = r.bool_true()
# if not bf:
#     password = input("Введите пароль: ")
#
#     if password == "x":
#         DB_LOGIN = "123456789"
#         DB_NAME = "root"
#     else:
#         DB_LOGIN = "12341234rus"
#         DB_NAME = "root"


class Setting(BaseSettings):

    db_url: str = f"mysql+aiomysql://root:123456789@localhost/demofayzulloev222"

    api_v1_prefix: str = "/api/v1"

    db_echo: bool = True

    # db_url: str = "mysql+aiosmysql:///./db.sqlite3"


# f"mysql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_PORT}/{self.DB_NAME}"
settings = Setting()
