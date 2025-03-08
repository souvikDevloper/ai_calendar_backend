from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.event import Event
from models.event import Event, EventCreate, EventUpdate

from services.database import get_db
from fastapi.security import OAuth2PasswordBearer
from models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
event_router = APIRouter()

# ✅ Create a new event
@event_router.post("/create/")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Event(
        user_id=event.user_id,
        title=event.title,
        start_time=event.start_time,
        end_time=event.end_time,
        priority=event.priority,
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return {"message": "Event created successfully", "event": new_event}

# ✅ Retrieve all events for a user
@event_router.get("/user/{user_id}")
def get_user_events(user_id: int, db: Session = Depends(get_db)):
    events = db.query(Event).filter(Event.user_id == user_id).all()
    if not events:
        raise HTTPException(status_code=404, detail="No events found")
    return events

# ✅ Retrieve a specific event by ID
@event_router.get("/{event_id}")
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

# ✅ Update an event
@event_router.put("/{event_id}")
def update_event(event_id: int, updated_event: EventUpdate, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    event.title = updated_event.title
    event.start_time = updated_event.start_time
    event.end_time = updated_event.end_time
    event.priority = updated_event.priority

    db.commit()
    return {"message": "Event updated successfully"}

# ✅ Delete an event
@event_router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(event)
    db.commit()
    return {"message": "Event deleted successfully"}
