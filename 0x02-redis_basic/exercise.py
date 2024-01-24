#!/usr/bin/env python3
"""cache class"""

import redis
import uuid
from typing import Union, Callable, Any


class Cache:
    """declaring Cache class"""
    def __init__(self):
        """initializing Cache with an instance
        of Redis()
        then flushes the db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data stores it in redis and returns its id as Key"""
        newKey = str(uuid.uuid4())
        self._redis.set(newKey, data)
        return newKey

    def get(self, key: str, fn: Callable) -> Union[str, int, None]:
        """retrives a value for the passed key
        then uses fn to convert the value to its appropriate
        type return the value if found or None"""
        if not key:
            return None
        binaryData = self._redis.get(key)
        if not binaryData:
            return None
        data = fn(binaryData)
        return data

    def get_str(self, binaryData: bytes) -> str:
        """converts binaryData to string and returns it"""
        return binaryData.decode('utf-8')

    def get_int(self, binaryData: bytes) -> int:
        """converts binaryData to int and returns it"""
        return int(binaryData)
