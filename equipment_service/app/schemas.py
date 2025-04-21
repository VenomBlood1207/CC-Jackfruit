from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .models import EquipmentType

class EquipmentBase(BaseModel):
    name: str
    equipment_type: EquipmentType
    quantity: int = Field(gt=0)
    condition: str
    purchase_date: datetime
    cost: float = Field(gt=0)
    last_maintenance: Optional[datetime] = None

class EquipmentCreate(EquipmentBase):
    pass

class EquipmentUpdate(BaseModel):
    name: Optional[str] = None
    equipment_type: Optional[EquipmentType] = None
    quantity: Optional[int] = Field(None, gt=0)
    condition: Optional[str] = None
    cost: Optional[float] = Field(None, gt=0)
    last_maintenance: Optional[datetime] = None
    is_available: Optional[bool] = None

class EquipmentRead(EquipmentBase):
    id: int
    is_available: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True