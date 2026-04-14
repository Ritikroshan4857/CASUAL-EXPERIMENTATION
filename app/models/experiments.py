from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime

from app.db.base import Base


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    variants = Column(JSON, nullable=False)
    status = Column(String, default="active")
    created_at = Column(DateTime, default=datetime.utcnow)