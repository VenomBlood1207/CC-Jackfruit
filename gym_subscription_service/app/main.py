from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from . import schemas
from .database import get_db
from typing import List
from datetime import datetime

app = FastAPI(title="Gym Subscription Management Service")

@app.post("/subscriptions/", response_model=schemas.GymSubscriptionRead)
def create_subscription(subscription: schemas.GymSubscriptionCreate, db: Session = Depends(get_db)):
    db_subscription = models.GymSubscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

@app.get("/subscriptions/", response_model=List[schemas.GymSubscriptionRead])
def read_subscriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subscriptions = db.query(models.GymSubscription).offset(skip).limit(limit).all()
    return subscriptions

@app.get("/subscriptions/{subscription_id}", response_model=schemas.GymSubscriptionRead)
def read_subscription(subscription_id: int, db: Session = Depends(get_db)):
    subscription = db.query(models.GymSubscription).filter(models.GymSubscription.id == subscription_id).first()
    if subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription

@app.put("/subscriptions/{subscription_id}", response_model=schemas.GymSubscriptionRead)
def update_subscription(subscription_id: int, subscription: schemas.GymSubscriptionUpdate, db: Session = Depends(get_db)):
    db_subscription = db.query(models.GymSubscription).filter(models.GymSubscription.id == subscription_id).first()
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    for key, value in subscription.dict(exclude_unset=True).items():
        setattr(db_subscription, key, value)
    
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

@app.delete("/subscriptions/{subscription_id}")
def cancel_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = db.query(models.GymSubscription).filter(models.GymSubscription.id == subscription_id).first()
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    db_subscription.is_active = False
    db.commit()
    return {"message": "Subscription cancelled successfully"}