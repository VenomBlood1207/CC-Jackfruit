from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime
from shared.database import Base
import enum
from datetime import datetime

class Specialization(str, enum.Enum):
    badminton = "badminton"
    volleyball = "volleyball"
    basketball = "basketball"

class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)
    specialization = Column(Enum(Specialization))
    contact_number = Column(String(20))
    email = Column(String(100), unique=True)
    is_active = Column(Boolean, default=True)
    years_of_experience = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)