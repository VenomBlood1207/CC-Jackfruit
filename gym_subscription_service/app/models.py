from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, Enum
from shared.database import Base
import enum
from datetime import datetime

class SubscriptionType(str, enum.Enum):
    monthly = "monthly"
    quarterly = "quarterly"
    yearly = "yearly"

class GymSubscription(Base):
    __tablename__ = "gym_subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    member_name = Column(String(100), nullable=False)
    member_email = Column(String(100), nullable=False)
    subscription_type = Column(Enum(SubscriptionType), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    amount_paid = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    contact_number = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)