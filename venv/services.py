import redis
from services.scheduler import suggest_smart_meeting


redis_client = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)

def get_meeting_suggestion(user_id, duration=30):
    cache_key = f"meeting_suggestion:{user_id}:{duration}"
    cached_result = redis_client.get(cache_key)

    if cached_result:
        return cached_result

    best_time = suggest_smart_meeting(user_id, duration)
    redis_client.setex(cache_key, 600, best_time)
    return best_time
