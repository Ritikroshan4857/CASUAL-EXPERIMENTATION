import numpy as np, pandas as pd
from datetime import datetime, timedelta

CONVERSION_RATES = {"control": 0.05, "treatment": 0.065}
PURCHASE_AMOUNT_MEAN = {"control": 45.0, "treatment": 52.0}



def simulate_experiment(n_users=20000, n_days=14):
    events = []
    start = datetime.now() - timedelta(days=n_days)
    
    for i in range(n_users):
        user_id = f"user_{i:06d}"
        variant = "control" if i % 2 == 0 else "treatment"
        
        # Simulate page view (all users)
        ts = start + timedelta(
            seconds=np.random.randint(0, n_days * 86400))
        events.append({
            "user_id": user_id, "variant": variant,
            "event_type": "page_view", "value": None, "timestamp": ts
        })
        
        # Simulate conversion (only some users)
        converted = np.random.random() < CONVERSION_RATES[variant]
        if converted:
            amount = np.random.normal(
                PURCHASE_AMOUNT_MEAN[variant], 15)
            events.append({
                "user_id": user_id, "variant": variant,
                "event_type": "purchase",
                "value": max(0, amount),
                "timestamp": ts + timedelta(minutes=np.random.randint(1, 30))
            })
    
    return pd.DataFrame(events)