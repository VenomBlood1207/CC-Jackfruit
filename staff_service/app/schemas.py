from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from .models import Specialization

class StaffBase(BaseModel):
    name: str
    role: str
    specialization: Optional[Specialization]
    contact_number: Optional[str]
    email: EmailStr
    years_of_experience: Optional[int]

class StaffCreate(StaffBase):
    pass

class StaffRead(StaffBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class StaffUpdate(StaffBase):
    name: Optional[str] = None
    role: Optional[str] = None
    specialization: Optional[Specialization] = None
    contact_number: Optional[str] = None
    email: Optional[EmailStr] = None
    years_of_experience: Optional[int] = None