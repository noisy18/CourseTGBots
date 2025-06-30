from datetime import timedelta
import os
from fastapi import APIRouter, Depends
from dotenv import load_dotenv

from schemas.token import TokenRequest, TokenResponse
from utils.create_token import create_access_token
from utils.docs.tags import TOKENS
from db.repositoies.token import TokenRepository

# Загружаем переменные из .env
load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

router = APIRouter(
    prefix="/tokens",
    tags=[TOKENS]
)

repo = TokenRepository()

@router.post("", summary="Create token")
async def post(token_request: TokenRequest) -> TokenResponse:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": token_request.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("", summary="Get token by email")
async def get(email: str = Depends(repo.get_current_email)):
    return {"access": True, "email": email}