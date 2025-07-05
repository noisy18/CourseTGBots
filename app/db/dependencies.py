from app.db.session import async_session_local
from app.db.db_manager import DB

async def get_db() -> DB:
    async with async_session_local() as session:
        try:
            yield DB(session)
        finally:
            await session.close()