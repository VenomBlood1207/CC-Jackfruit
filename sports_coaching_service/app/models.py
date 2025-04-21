from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, Enum, ForeignKey
from shared.database import Base
import enum
from datetime import datetime

class SportType(str, enum.Enum):
    badminton = "badminton"
    volleyball = "volleyball"
    basketball = "basketball"

class CoachingSession(Base):
    __tablename__ = "coaching_sessions"

    id = Column(Integer, primary_key=True, index=True)
    sport_type = Column(Enum(SportType), nullable=False)
    coach_id = Column(Integer, nullable=False)  # References staff service
    session_date = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    max_participants = Column(Integer, nullable=False)
    current_participants = Column(Integer, default=0)
    price_per_person = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SessionBooking(Base):
    __tablename__ = "session_bookings"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("coaching_sessions.id"))
    participant_name = Column(String(100), nullable=False)
    participant_email = Column(String(100), nullable=False)
    booking_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)