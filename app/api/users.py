from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.dependencies import get_db
from app.utils.docs.tags import USERS
from app.schemas.user import UserResponseSchema, UserCreateSchema
from app.db.db_manager import DB

router = APIRouter(
    tags=[USERS]
)

@router.post("/register", response_model=UserResponseSchema)
async def post(user_data: UserCreateSchema, db: DB = Depends(get_db)):
    user = await db.users.get_user_by_email(email=user_data.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await db.users.create_user(user=user_data)
    return new_user


@router.get("/me/{user_id}", response_model=UserResponseSchema)
async def get(user_id: int, db: DB = Depends(get_db)):
    user = await db.users.get_user_by_id(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user