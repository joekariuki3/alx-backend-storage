#!/usr/bin/env python3
"""implementing expiring web cache with redis"""

import redis
import requests


def get_page(url: str) -> str:
    """Implementing an expiring web cache and tracker"""
    r = redis.Redis()
    key = f"count:{url}"
    r.incr(key)

    """check if catched"""
    cachedContent = r.get(key)
    if cachedContent:
        return cachedContent.decode('utf-8')

    """if not catched"""
    response = requests.get(url)
    """Cache the result with an expiration time of 10 seconds"""
    r.setex(key, 10, response.text)

    return response.text
