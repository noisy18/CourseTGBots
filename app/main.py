from fastapi import FastAPI
from contextlib import asynccontextmanager
import time

from app.api.tokens import router as token_router
from app.api.users import router as user_router
from app.api.notes import router as notes_router
from app.db.session import create_tables, delete_tables, close_engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Удаляем старые таблицы только если они существуют
        try:
            await delete_tables()
            print("База очищена")
        except Exception as e:
            print(f"Ошибка при очистке базы (возможно, таблицы не существовали): {e}")
        
        await create_tables()
        print("База готова к работе")
    except Exception as e:
        print(f"Ошибка инициализации к БД: {e}")
        # Не завершаем приложение сразу, даем возможность переподключиться
        time.sleep(5)  # Даем время PostgreSQL полностью запуститься
        await create_tables()  # Повторная попытка
    yield
    
    try:
        await close_engine()
        print("Подключение в БД закрыто")
    except Exception as e:
        print(f"Ошибка при закрытии подлюченией: {e}")

app = FastAPI(lifespan=lifespan)
app.include_router(token_router)
app.include_router(user_router)
app.include_router(notes_router)