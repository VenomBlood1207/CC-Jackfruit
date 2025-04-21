from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from . import schemas
from .database import get_db
from typing import List

app = FastAPI(title="Equipment Management Service")

@app.post("/equipment/", response_model=schemas.EquipmentRead)
def create_equipment(equipment: schemas.EquipmentCreate, db: Session = Depends(get_db)):
    db_equipment = models.Equipment(**equipment.dict())
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment

@app.get("/equipment/", response_model=List[schemas.EquipmentRead])
def read_equipment(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    equipment = db.query(models.Equipment).offset(skip).limit(limit).all()
    return equipment

@app.get("/equipment/{equipment_id}", response_model=schemas.EquipmentRead)
def read_equipment_by_id(equipment_id: int, db: Session = Depends(get_db)):
    equipment = db.query(models.Equipment).filter(models.Equipment.id == equipment_id).first()
    if equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

@app.put("/equipment/{equipment_id}", response_model=schemas.EquipmentRead)
def update_equipment(equipment_id: int, equipment: schemas.EquipmentUpdate, db: Session = Depends(get_db)):
    db_equipment = db.query(models.Equipment).filter(models.Equipment.id == equipment_id).first()
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    
    for key, value in equipment.dict(exclude_unset=True).items():
        setattr(db_equipment, key, value)
    
    db.commit()
    db.refresh(db_equipment)
    return db_equipment

@app.delete("/equipment/{equipment_id}")
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    db_equipment = db.query(models.Equipment).filter(models.Equipment.id == equipment_id).first()
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    
    db_equipment.is_available = False
    db.commit()
    return {"message": "Equipment deactivated successfully"}