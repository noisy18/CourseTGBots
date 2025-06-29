from pydantic import BaseModel, EmailStr

# Схема для запроса токена
class TokenRequest(BaseModel):
    email: EmailStr

# Схема ответа с токеном
class TokenResponse(BaseModel):
    access_token: str
    token_type: str