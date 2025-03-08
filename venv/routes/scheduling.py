from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.database import get_db
from services.scheduler import suggest_smart_meeting
from models.user import User
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
scheduling_router = APIRouter()

@scheduling_router.get("/smart_suggest_meeting/")
def get_smart_meeting(user_id: int, db: Session = Depends(get_db)):
    return suggest_smart_meeting(user_id, db)
