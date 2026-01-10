from logging.config import fileConfig
import os

from alembic import context
from sqlalchemy import engine_from_config, pool
from src.database.base import Base
from src.database.session import engine  # import your app engine
from src.database import models  # <- this must import all model classes

# Alembic config object
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Use your app’s metadata for autogenerate
target_metadata = Base.metadata

def run_migrations_offline():
    url = str(engine.url)  # use the engine URL directly
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    # Use your existing engine from session.py
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True  # optional: detects type changes
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
