from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from api.tokens import router as token_router
from api.users import router as user_router
from db.session import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(token_router)
app.include_router(user_router)

# Тестовый запуск проекта
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)