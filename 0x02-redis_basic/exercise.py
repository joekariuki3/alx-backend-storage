#!/usr/bin/env python3
"""cache class"""

import redis
import uuid
from typing import Union


class Cache:
    """declaring Cache class"""
    def __init__(self):
        """initializing Cache with an instance
        of Redis()
        then flushes the db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data stores it in resid and returns its id as Key"""
        newKey = str(uuid.uuid4())
        self._redis.set(newKey, data)
        return newKey
