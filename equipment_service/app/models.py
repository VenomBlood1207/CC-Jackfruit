from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime, Float
from shared.database import Base
import enum
from datetime import datetime

class EquipmentType(str, enum.Enum):
    badminton = "badminton"
    volleyball = "volleyball"
    basketball = "basketball"
    general = "general"

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    equipment_type = Column(Enum(EquipmentType), nullable=False)
    quantity = Column(Integer, nullable=False)
    condition = Column(String(50), nullable=False)
    purchase_date = Column(DateTime, nullable=False)
    last_maintenance = Column(DateTime)
    cost = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)