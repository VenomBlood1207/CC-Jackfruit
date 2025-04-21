from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
import sys
from pathlib import Path

# Add the parent directory to PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent.parent))

# Import the shared database configuration
from shared.database import get_db_url
from staff_service.app import models as staff_models
from equipment_service.app import models as equipment_models
from gym_subscription_service.app import models as subscription_models
from sports_coaching_service.app import models as coaching_models

# This is the Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add your model's MetaData objects here for 'autogenerate' support
target_metadata = [
    staff_models.Base.metadata,
    equipment_models.Base.metadata,
    subscription_models.Base.metadata,
    coaching_models.Base.metadata,
]

def get_url():
    """Get database URL based on environment variables"""
    return get_db_url(os.getenv("SERVICE_NAME", "staff_service"))

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()