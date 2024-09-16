import asyncio
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.database import models


class DataBase:
    def __init__(self, url: str = "sqlite+aiosqlite:///database.sqlite3") -> None:
        self.url: str = url
        self.engine: AsyncEngine = create_async_engine(self.url, echo=True)
        self._session_factory: AsyncSession = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def setup(self) -> None:
        """Create tables in the database."""
        async with self.engine.begin() as conn:
            await conn.run_sync(models.Base.metadata.create_all)

    async def get_session(self) -> AsyncGenerator[AsyncSession]:
        """Returns an async session."""
        async with self._session_factory() as session:
            yield session


db = DataBase()
