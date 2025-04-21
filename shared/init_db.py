from sqlalchemy import create_engine
from database import get_db_url
import importlib
import os

def init_database(service_name: str):
    """Initialize database for a specific service"""
    print(f"Initializing database for {service_name}")
    
    # Import the models module for the service
    try:
        # Dynamically import models for the service
        models = importlib.import_module(f"{service_name}.app.models")
        print(f"Successfully imported models for {service_name}")
    except ModuleNotFoundError as e:
        print(f"Could not import models for {service_name}: {e}")

    # Create database engine
    engine = create_engine(get_db_url(service_name))
    
    # Create all tables
    try:
        models.Base.metadata.create_all(bind=engine)
        print(f"Successfully created tables for {service_name}")
    except Exception as e:
        print(f"Error creating tables for {service_name}: {e}")

if __name__ == "__main__":
    # Initialize databases for all services
    services = [
        "staff_service",
        "equipment_service",
        "gym_subscription_service",
        "sports_coaching_service"
    ]
    
    for service in services:
        init_database(service)