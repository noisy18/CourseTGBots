from typing import TypeVar, Generic, Type, Optional, Any, List, ClassVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, insert
from sqlalchemy.orm import DeclarativeMeta, Load
from sqlalchemy.engine import Result
from sqlalchemy.orm.interfaces import LoaderOption

ModelType = TypeVar("ModelType", bound=DeclarativeMeta)


class BaseRepository(Generic[ModelType]):
    model: Type[ModelType]
    options: Optional[List[LoaderOption]] = None

    def init(self, session: AsyncSession):
        if not hasattr(self, "model"):
            raise ValueError("Subclasses must define class-level 'model'")
        self.session = session

    def _with_related(self) -> List[Load]:
        return self.options or []

    async def get_by_id(self, id_: int, with_related: bool = False) -> Optional[ModelType]:
        stmt = select(self.model).where(self.model.id == id_)
        if with_related:
            stmt = stmt.options(*self._with_related())
        result: Result = await self.session.execute(statement=stmt)
        return result.scalar_one_or_none()

    async def get_all(self) -> List[ModelType]:
        stmt = select(self.model)
        result: Result = await self.session.execute(statement=stmt)
        return result.scalars().all()

    async def create(self, returning: bool = False, **kwargs) -> ModelType:
        stmt = insert(self.model).values(**kwargs)
        if returning:
            stmt = stmt.returning(self.model)
        result: Result = await self.session.execute(statement=stmt)
        await self.session.commit()
        if returning:
            return result.scalar_one()

    async def update_by_id(self, id_: Any, returning: bool = True, **data) -> Optional[ModelType]:
        stmt = (
            update(self.model)
            .where(self.model.id == id_)
            .values(**data)
        )
        if returning:
            stmt = stmt.returning(self.model)

        result: Result = await self.session.execute(statement=stmt)
        await self.session.commit()
        return result.scalar_one_or_none() if returning else None

    async def delete_by_id(self, id_: Any) -> None:
        stmt = delete(self.model).where(self.model.id == id_)
        await self.session.execute(stmt)
        await self.session.commit()

    async def exists(self, **filters) -> bool:
        stmt = select(self.model).filter_by(**filters)
        result = await self.session.execute(statement=stmt)
        return result.scalar_one_or_none() is not None

    async def filter_by(self, **filters) -> List[ModelType]:
        stmt = select(self.model).filter_by(**filters)
        result = await self.session.execute(statement=stmt)
        return result.scalars().all()