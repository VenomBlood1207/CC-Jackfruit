from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
from typing import List
from datetime import datetime

app = FastAPI(title="Sports Coaching Service")

@app.post("/sessions/", response_model=schemas.CoachingSessionRead)
def create_session(session: schemas.CoachingSessionCreate, db: Session = Depends(get_db)):
    db_session = models.CoachingSession(**session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

@app.get("/sessions/", response_model=List[schemas.CoachingSessionRead])
def read_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sessions = db.query(models.CoachingSession).offset(skip).limit(limit).all()
    return sessions

@app.get("/sessions/{session_id}", response_model=schemas.CoachingSessionRead)
def read_session(session_id: int, db: Session = Depends(get_db)):
    session = db.query(models.CoachingSession).filter(models.CoachingSession.id == session_id).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Coaching session not found")
    return session

@app.post("/bookings/", response_model=schemas.SessionBookingRead)
def create_booking(booking: schemas.SessionBookingCreate, db: Session = Depends(get_db)):
    session = db.query(models.CoachingSession).filter(models.CoachingSession.id == booking.session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Coaching session not found")
    
    if session.current_participants >= session.max_participants:
        raise HTTPException(status_code=400, detail="Session is full")
    
    db_booking = models.SessionBooking(**booking.dict())
    session.current_participants += 1
    
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@app.delete("/bookings/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(models.SessionBooking).filter(models.SessionBooking.id == booking_id).first()
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    session = db.query(models.CoachingSession).filter(models.CoachingSession.id == booking.session_id).first()
    if session:
        session.current_participants -= 1
    
    booking.is_active = False
    db.commit()
    return {"message": "Booking cancelled successfully"}