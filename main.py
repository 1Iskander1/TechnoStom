# 5 таблица клиентов
# 6 таблица заказов
# 7 таблица учета материалов
import uvicorn
from fastapi import FastAPI

from api_v1 import router as router_v1
from core.config import settings

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#
#     async with db_helper.engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
#     yield


app = FastAPI()

app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


# @app.get("/")
# def hello_index():
#     return {
#         "message": "Hello index!",
#     }


if __name__ == "__main__":

    uvicorn.run("main:app", reload=True)
