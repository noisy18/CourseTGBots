from app.db.session import async_session_local
from sqlalchemy.ext.asyncio import AsyncSession

async def get_db() -> AsyncSession:
    async with async_session_local() as session:
        try:
            yield session
        finally:
            await session.close()