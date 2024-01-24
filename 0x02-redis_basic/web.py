#!/usr/bin/env python3
"""implementing expiring web cache with redis"""

import requests
import redis
import time
from functools import wraps


def track_access_count(func):
    """do the increment everytime the url is accessed"""
    @wraps(func)
    def wrapper(url):
        # Initialize Redis client
        redis_client = redis.Redis()

        # Increment the access count for the URL
        count_key = f"count:{url}"
        redis_client.incr(count_key)

        return func(url)

    return wrapper


def cache_result(expiration_time):
    """decorator to save/cache the url page for 10 seconds"""
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            # Initialize Redis client
            redis_client = redis.Redis()

            # Check if the page is already cached
            cache_key = f"cache:{url}"
            cached_content = redis_client.get(cache_key)

            if cached_content is not None:
                return cached_content.decode('utf-8')

            # If not cached, fetch the page content using the original function
            response_text = func(url)

            # Cache the result with the specified expiration time
            redis_client.setex(cache_key, expiration_time, response_text)

            return response_text

        return wrapper
    return decorator


@track_access_count
@cache_result(expiration_time=10)
def get_page(url: str) -> str:
    """Fetch the page content using requests"""
    response = requests.get(url)
    return response.text
