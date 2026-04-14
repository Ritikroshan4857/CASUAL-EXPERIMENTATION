import redis

# Connect to Redis
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)


def get_assignment(user_id: int, experiment_id: str):
    """
    Get assignment from Redis
    """
    key = f"exp:{experiment_id}:user:{user_id}"
    return redis_client.get(key)


def set_assignment(user_id: int, experiment_id: str, variant: str, ttl: int = 3600):
    """
    Store assignment in Redis with TTL
    """
    key = f"exp:{experiment_id}:user:{user_id}"
    redis_client.set(key, variant, ex=ttl)