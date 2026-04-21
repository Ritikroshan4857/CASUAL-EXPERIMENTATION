from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, BigInteger
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime
from app.db.base import Base
class Experiment(Base):
    __tablename__ = "experiments"
    id = Column(String(64), primary_key=True)
    name = Column(String(255))
    variants = Column(JSONB)
    status = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(64))
    experiment_id = Column(String(64))
    variant = Column(String(32))
class ExperimentEvent(Base):
    __tablename__ = "experiment_events"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    user_id = Column(String(64), nullable=False)
    experiment_id = Column(String(64), ForeignKey("experiments.id"))
    variant = Column(String(32), nullable=False)
    event_type = Column(String(64), nullable=False)
    value = Column(Float, nullable=True)
    event_metadata = Column(JSONB, nullable=True)