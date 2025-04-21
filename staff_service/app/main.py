from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from . import schemas
from .database import get_db
from typing import List

app = FastAPI(title="Staff Management Service")

@app.post("/staff/", response_model=schemas.StaffRead)
def create_staff(staff: schemas.StaffCreate, db: Session = Depends(get_db)):
    db_staff = models.Staff(**staff.dict())
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

@app.get("/staff/", response_model=List[schemas.StaffRead])
def read_staff(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    staff = db.query(models.Staff).offset(skip).limit(limit).all()
    return staff

@app.get("/staff/{staff_id}", response_model=schemas.StaffRead)
def read_staff_by_id(staff_id: int, db: Session = Depends(get_db)):
    staff = db.query(models.Staff).filter(models.Staff.id == staff_id).first()
    if staff is None:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff

@app.put("/staff/{staff_id}", response_model=schemas.StaffRead)
def update_staff(staff_id: int, staff: schemas.StaffUpdate, db: Session = Depends(get_db)):
    db_staff = db.query(models.Staff).filter(models.Staff.id == staff_id).first()
    if db_staff is None:
        raise HTTPException(status_code=404, detail="Staff not found")
    
    for key, value in staff.dict(exclude_unset=True).items():
        setattr(db_staff, key, value)
    
    db.commit()
    db.refresh(db_staff)
    return db_staff

@app.delete("/staff/{staff_id}")
def delete_staff(staff_id: int, db: Session = Depends(get_db)):
    db_staff = db.query(models.Staff).filter(models.Staff.id == staff_id).first()
    if db_staff is None:
        raise HTTPException(status_code=404, detail="Staff not found")
    
    db_staff.is_active = False
    db.commit()
    return {"message": "Staff deactivated successfully"}