from shared.database import get_db_session
import os

SERVICE_NAME = "sports_coaching_service"
SessionLocal = get_db_session(SERVICE_NAME)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()