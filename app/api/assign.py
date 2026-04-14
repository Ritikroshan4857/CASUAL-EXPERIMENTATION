from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.assignment import assign_variant
from app.core.redis_client import redis_client
from app.models.experiment import Experiment