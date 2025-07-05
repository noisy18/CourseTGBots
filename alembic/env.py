import os
import sys
import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context

from app.config import get_settings

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app.db.base import Base
from app.models.note import Note
from app.models.user import User

config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

settings = get_settings()
DATABASE_URL = str(settings.DATABASE_URL)
SYNC_DATABASE_URL = str(settings.SYNC_DATABASE_URL)

def run_migrations_offline():
    """Запуск миграций в offline-режиме (генерация SQL)."""
    context.configure(
        url=SYNC_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_async_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    async def do_run_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(run_sync_migrations)

    def run_sync_migrations(sync_conn):
        context.configure(
            connection=sync_conn,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

    asyncio.run(do_run_migrations())



# Вызываем нужный режим
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
