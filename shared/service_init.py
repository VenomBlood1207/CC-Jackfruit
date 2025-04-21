import os
import importlib
from sqlalchemy import create_engine
from alembic.config import Config
from alembic import command
from database import get_db_url

def init_service():
    """Initialize service database and run migrations"""
    service_name = os.getenv("SERVICE_NAME")
    if not service_name:
        raise ValueError("SERVICE_NAME environment variable must be set")

    print(f"Initializing service: {service_name}")

    # Import service models
    try:
        models = importlib.import_module(f"service.app.models")
    except ImportError as e:
        print(f"Error importing models: {e}")
        raise

    # Create database engine
    engine = create_engine(get_db_url(service_name))

    # Create all tables
    try:
        models.Base.metadata.create_all(bind=engine)
        print("Created database tables")
    except Exception as e:
        print(f"Error creating tables: {e}")
        raise

    # Run Alembic migrations
    try:
        alembic_cfg = Config("shared/alembic.ini")
        command.upgrade(alembic_cfg, "head")
        print("Applied database migrations")
    except Exception as e:
        print(f"Error applying migrations: {e}")
        raise

    print(f"Service {service_name} initialized successfully")

if __name__ == "__main__":
    init_service()