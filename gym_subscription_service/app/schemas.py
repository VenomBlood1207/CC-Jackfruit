from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from .models import SubscriptionType

class GymSubscriptionBase(BaseModel):
    member_name: str
    member_email: EmailStr
    subscription_type: SubscriptionType
    start_date: datetime
    end_date: datetime
    amount_paid: float = Field(gt=0)
    contact_number: Optional[str] = None

class GymSubscriptionCreate(GymSubscriptionBase):
    pass

class GymSubscriptionUpdate(BaseModel):
    member_name: Optional[str] = None
    subscription_type: Optional[SubscriptionType] = None
    end_date: Optional[datetime] = None
    amount_paid: Optional[float] = Field(None, gt=0)
    contact_number: Optional[str] = None
    is_active: Optional[bool] = None

class GymSubscriptionRead(GymSubscriptionBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True