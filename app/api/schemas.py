from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EventCreate(BaseModel):
    user_id: str
    experiment_id: str
    variant: str
    event_type: str
    value: Optional[float] = None
    timestamp: Optional[datetime] = None




