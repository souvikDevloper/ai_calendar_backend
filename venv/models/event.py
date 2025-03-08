from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from services.database import Base
from pydantic import BaseModel
from datetime import datetime

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    priority = Column(Integer, default=1)

# ✅ Pydantic Schema for Event Creation (Request Validation)
class EventCreate(BaseModel):
    user_id: int
    title: str
    start_time: datetime
    end_time: datetime
    priority: int = 1

# ✅ Pydantic Schema for Event Update
class EventUpdate(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    priority: int = 1
