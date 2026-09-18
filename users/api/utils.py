import secrets
from django.core.cache import cache


def generate_verification_token(user_id: int) -> str:
    token = secrets.token_urlsafe(32)
    cache_key = f"email_verify:{token}"
    cache.set(cache_key, user_id, timeout=900)
    return token