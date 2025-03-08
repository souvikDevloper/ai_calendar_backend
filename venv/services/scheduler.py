import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from services.database import get_db
from sqlalchemy.orm import Session
from models.event import Event
from services.redis_cache import cache_meeting_suggestion, get_cached_meeting_suggestion
from sqlalchemy.orm import Session

def train_model(user_id, db: Session):
    events = db.query(Event).filter(Event.user_id == user_id).all()
    if not events:
        return None

    df = pd.DataFrame([{"start_time": e.start_time.hour, "end_time": e.end_time.hour, "priority": e.priority} for e in events])
    df["label"] = (df["priority"] > 1).astype(int)

    X = df[["start_time", "end_time"]]
    y = df["label"]

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model

def suggest_smart_meeting(user_id, db: Session, duration=30):
    model = train_model(user_id, db)
    if not model:
        return "No past data available. Suggesting default hours."

    time_slots = [(hour, hour + duration // 60) for hour in range(9, 17)]
    X_new = np.array(time_slots)
    predictions = model.predict_proba(X_new)[:, 1]
    best_time = time_slots[np.argmax(predictions)]

    return f"Suggested Meeting Time: {best_time[0]}:00 - {best_time[1]}:00"
def suggest_smart_meeting(user_id, db: Session, duration=30):
    cached_suggestion = get_cached_meeting_suggestion(user_id, duration)
    if cached_suggestion:
        return cached_suggestion  # Return cached result if available

    # AI-powered scheduling logic here...
    best_time = "Suggested Meeting: 14:00 - 15:00"  # Placeholder for AI logic

    cache_meeting_suggestion(user_id, duration, best_time)  # Store in cache
    return best_time