from fastapi import FastAPI
import uvicorn

from api.tokens import router as token_router

app = FastAPI()
app.include_router(token_router)

# Тестовый запуск проекта
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)