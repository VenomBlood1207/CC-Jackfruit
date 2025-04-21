from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import time
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError

load_dotenv()

def get_db_url(service_name: str) -> str:
    """Get database URL for specific service"""
    host = os.getenv(f"{service_name.upper()}_DB_HOST", "db")  # Change default to "db"
    database = os.getenv(f"{service_name.upper()}_DB_NAME", f"{service_name}")
    user = os.getenv(f"{service_name.upper()}_DB_USER", "postgres")
    password = os.getenv(f"{service_name.upper()}_DB_PASSWORD", "postgres")
    db_url = f"postgresql://{user}:{password}@{host}/{database}"
    print(f"[DEBUG] Database URL for {service_name}: {db_url}")
    return db_url

def get_db_session(service_name: str):
    """Create database session for specific service with retry mechanism"""
    SQLALCHEMY_DATABASE_URL = get_db_url(service_name)
    retries = 5
    for attempt in range(retries):
        try:
            engine = create_engine(SQLALCHEMY_DATABASE_URL)
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            print(f"[INFO] Successfully connected to the database for {service_name}")
            return SessionLocal
        except OperationalError as e:
            print(f"[ERROR] Database connection failed for {service_name}: {e}")
            if attempt < retries - 1:
                print(f"[INFO] Retrying connection ({attempt + 1}/{retries})...")
                time.sleep(5)  # Wait before retrying
            else:
                raise Exception(f"Failed to connect to the database for {service_name} after {retries} attempts") from e

Base = declarative_base()