from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.dependencies import get_db
from utils.docs.tags import USERS
from schemas.user import UserResponseSchema, UserCreateSchema
from db.repositoies.user import UserRepository

router = APIRouter(
    tags=[USERS]
)

repo = UserRepository()

@router.post("/register", response_model=UserResponseSchema)
async def post(user_data: UserCreateSchema, db: AsyncSession = Depends(get_db)):
    user = await repo.get_user_by_email(db, email=user_data.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await repo.create_user(db=db, user=user_data)
    new_user.uuid = str(new_user.uuid)
    return new_user

@router.get("/me/{user_id}", response_model=UserResponseSchema)
async def get(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await repo.get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.uuid = str(user.uuid)
    return user