# Redis basics

Python-based Redis exercises showing:

- A `Cache` class that counts method calls and records input/output history using decorators
- Type-converting getters (`get_str`, `get_int`)
- A simple web page cache with TTL and an access counter per URL

## Files

- `exercise.py`: `Cache` with decorators
  - `@count_calls`: increments `<qualname>` key per call
  - `@call_history`: appends to `<qualname>:inputs` and `<qualname>:outputs` lists
  - `store(data) -> str`: stores data under a UUID key
  - `get(key, fn=None)`: fetch with optional converter
  - `get_str` / `get_int`: helpers to decode types
  - `replay(func)`: prints call history from Redis
- `main.py`: small demo invoking `store` and printing history lists
- `web.py`: `get_page(url)` decorated to cache HTML for 10s and increment `count:<url>`

## Prerequisites

- Redis server running locally (`redis-server`)
- Python 3.8+
- Packages: `redis`, `requests` (install via repo-level `requirements.txt`)

## Run

Start Redis, then run the demos:

```
redis-server &
python main.py
```

Try the page cache:

```
python -c "from web import get_page; print(get_page('https://example.com'))"
```

Inspect keys and lists:

```
redis-cli KEYS '*store*'
redis-cli LRANGE 'Cache.store:inputs' 0 -1
redis-cli LRANGE 'Cache.store:outputs' 0 -1
```

> [!WARNING]
> The demo `Cache.__init__` calls `FLUSHDB`, which clears the current Redis DB on start. Don’t run against a production instance.

## Notes

- For binary values from Redis, use `get(key, fn=cache.get_str)` or `get_int` to coerce types.
- The `count:<url>` key in `web.py` tracks how many times a URL was requested.
