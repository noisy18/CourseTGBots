from fastapi import FastAPI

from app.api.tokens import router as token_router
from app.api.users import router as user_router
from app.api.notes import router as notes_router

app = FastAPI()

app.include_router(token_router)
app.include_router(user_router)
app.include_router(notes_router)