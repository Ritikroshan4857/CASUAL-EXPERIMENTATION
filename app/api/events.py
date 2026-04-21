from fastapi import APIRouter
from app.api.schemas import EventCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.crud import create_event_db
from app.api.schemas import EventCreate


router = APIRouter()

@router.post("/events")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    return create_event_db(db, event)