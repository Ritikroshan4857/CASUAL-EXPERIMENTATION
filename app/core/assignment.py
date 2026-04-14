import hashlib
def assign_variant(user_id: str, experiment_id:str, variants: list[str]) -> str:
    salt = f"{experiment_id}:{user_id}"
    hash_val = int(hashlib.md5(salt.encode()).hexdigest(), 16)
    return variants[hash_val % len(variants)]