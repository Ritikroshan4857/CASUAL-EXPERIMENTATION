from app.db.models import ExperimentEvent
def create_event_db(db, event):
    db_event = ExperimentEvent(
        user_id=event.user_id,
        experiment_id=event.experiment_id,
        variant=event.variant,
        event_type=event.event_type,
        value=event.value,
        timestamp=event.timestamp
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event