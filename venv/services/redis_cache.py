import redis
from config import REDIS_HOST, REDIS_PORT

# Initialize Redis connection
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def cache_meeting_suggestion(user_id, duration, suggestion):
    """
    Cache the AI-powered meeting suggestion for a specific user and duration.
    """
    cache_key = f"meeting_suggestion:{user_id}:{duration}"
    redis_client.setex(cache_key, 600, suggestion)  # Cache for 10 minutes

def get_cached_meeting_suggestion(user_id, duration):
    """
    Retrieve cached meeting suggestion if available.
    """
    cache_key = f"meeting_suggestion:{user_id}:{duration}"
    return redis_client.get(cache_key)

def cache_user_token(user_id, token):
    """
    Cache user authentication token for session management.
    """
    cache_key = f"user_token:{user_id}"
    redis_client.setex(cache_key, 3600, token)  # Cache for 1 hour

def get_cached_user_token(user_id):
    """
    Retrieve cached user token.
    """
    cache_key = f"user_token:{user_id}"
    return redis_client.get(cache_key)
