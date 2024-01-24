#!/usr/bin/env python3
"""cache class"""

import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator to count total number of times methods has been called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """get qualified name of the method"""
        key = method.__qualname__
        """do the increment"""
        self._redis.incr(key)
        """call the original method and return its results"""
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """keep a record of all the inputs and outputs of a method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Get the qualified name of the method"""
        key = method.__qualname__

        """Create input and output list keys"""
        inputs_key = f"{key}:inputs"
        outputs_key = f"{key}:outputs"

        """Store input arguments using rpush"""
        self._redis.rpush(inputs_key, str(args))

        """Call the original method to get the output"""
        result = method(self, *args, **kwargs)

        """Store the output using rpush"""
        self._redis.rpush(outputs_key, str(result))

        return result

    return wrapper


class Cache:
    """declaring Cache class"""
    def __init__(self):
        """initializing Cache with an instance
        of Redis()
        then flushes the db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data stores it in redis and returns its id as Key"""
        newKey = str(uuid.uuid4())
        self._redis.set(newKey, data)
        return newKey

    def get(self, key: str, fn=None) -> Union[str, int, None]:
        """retrives a value for the passed key
        then uses fn to convert the value to its appropriate
        type return the value if found or None"""
        if not key:
            return None
        binaryData = self._redis.get(key)
        if not binaryData:
            return None
        if fn:
            return fn(binaryData)
        return binaryData

    def get_str(self, binaryData: bytes) -> str:
        """converts binaryData to string and returns it"""
        return binaryData.decode('utf-8')

    def get_int(self, binaryData: bytes) -> int:
        """converts binaryData to int and returns it"""
        return int(binaryData)

    def replay(self, func):
        """display the inputs and outputs of a function that are
        stored in redis"""

        """Get the qualified name of the function"""
        key = func.__qualname__

        """Create input and output list keys"""
        inputs_key = f"{key}:inputs"
        outputs_key = f"{key}:outputs"

        """Retrieve input and output history from Redis"""
        inputs_history = cache_instance._redis.lrange(inputs_key, 0, -1)
        outputs_history = cache_instance._redis.lrange(outputs_key, 0, -1)

        """Display the history of calls"""
        print(f"{key} was called {len(inputs_history)} times:")

        for inputs, output in zip(inputs_history, outputs_history):
            """Convert inputs and output from strings to
            their respective types"""
            inputs = eval(inputs.decode())
            output = eval(output.decode())

            """Display the function call details"""
            print(f"{key}(*{inputs}) -> {output}")
