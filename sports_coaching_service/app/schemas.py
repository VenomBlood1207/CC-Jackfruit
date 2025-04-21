from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from .models import SportType

class CoachingSessionBase(BaseModel):
    sport_type: SportType
    coach_id: int
    session_date: datetime
    duration_minutes: int = Field(gt=0)
    max_participants: int = Field(gt=0)
    price_per_person: float = Field(gt=0)

class CoachingSessionCreate(CoachingSessionBase):
    pass

class CoachingSessionUpdate(BaseModel):
    session_date: Optional[datetime] = None
    duration_minutes: Optional[int] = Field(None, gt=0)
    max_participants: Optional[int] = Field(None, gt=0)
    price_per_person: Optional[float] = Field(None, gt=0)
    is_active: Optional[bool] = None

class SessionBookingBase(BaseModel):
    session_id: int
    participant_name: str
    participant_email: EmailStr

class SessionBookingCreate(SessionBookingBase):
    pass

class SessionBookingRead(SessionBookingBase):
    id: int
    booking_date: datetime
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CoachingSessionRead(CoachingSessionBase):
    id: int
    current_participants: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    bookings: List[SessionBookingRead] = []

    class Config:
        orm_mode = True