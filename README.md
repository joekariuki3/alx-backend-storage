# ALX Backend Storage

Backend storage exercises and utilities covering three data systems:

- Relational: advanced MySQL/SQL features and patterns
- Document: MongoDB with shell snippets and Python helpers
- In-memory: Redis with Python decorators and simple web caching

> [!TIP]
> This repo is organized as standalone sub-projects. You can work on them independently based on the storage you’re learning or using.

## Repository structure

```
0x00-MySQL_Advanced/   # SQL scripts: tables, procedures, triggers, functions, views, indexes
0x01-NoSQL/            # MongoDB: shell scripts and Python helpers using PyMongo
0x02-redis_basic/      # Redis: Python cache helpers, decorators, and simple page cache
```

## Prerequisites

- Linux or macOS shell (tested on Linux)
- Python 3.8+ with pip
- MySQL 8.x (or MariaDB 10.5+) client/server
- MongoDB Community Server 4.4+ (mongosh or mongo shell)
- Redis Server 6.x+

Python packages (install once at repo root):

```
pip install -r requirements.txt
```

> [!NOTE]
> If you prefer manual installs: `pymongo`, `redis`, and `requests` are used by the Python examples.

## Quick start

### 1) MySQL Advanced (0x00-MySQL_Advanced)

Import datasets when needed, then run any script via the MySQL client:

```
mysql -u <user> -p < database.sql
mysql -u <user> -p < 0x00-MySQL_Advanced/metal_bands.sql
mysql -u <user> -p < 0x00-MySQL_Advanced/names.sql
mysql -u <user> -p < 0x00-MySQL_Advanced/3-glam_rock.sql
```

> [!TIP]
> Many tasks ship with init and main SQL files like `7-init.sql`, `11-main.sql` to help you seed and test your work quickly.

### 2) MongoDB NoSQL (0x01-NoSQL)

Run shell snippets with mongosh:

```
mongosh < 0x01-NoSQL/0-list_databases
mongosh < 0x01-NoSQL/2-insert
```

Run Python helpers and demos (requires MongoDB running locally at `mongodb://127.0.0.1:27017`):

```
python 0x01-NoSQL/8-main.py
python 0x01-NoSQL/9-main.py
python 0x01-NoSQL/10-main.py
python 0x01-NoSQL/11-main.py
```

### 3) Redis basics (0x02-redis_basic)

Start Redis locally, then run examples:

```
redis-server &
python 0x02-redis_basic/main.py
```

For the simple web cache demo (caches for 10s and tracks request count):

```
cd 0x02-redis_basic
python -c "from web import get_page; print(get_page('https://example.com'))"
cd -
```

## Sub-project highlights

- 0x00-MySQL_Advanced
  - Table design with constraints and enums
  - Triggers (e.g., stock decrement on order), stored procedures, scalar functions
  - Views and analytics queries (ranking, longevity), partial indexes
- 0x01-NoSQL
  - Mongo shell snippets for CRUD, filtering, and counts
  - PyMongo helpers for listing, inserting, updating topics, and querying by topic
- 0x02-redis_basic
  - Decorators for call counting and history logging using Redis lists
  - Getters with on-demand type conversion; simple page cache with TTL and access counters

## Troubleshooting

> [!WARNING]
> Ensure each datastore is running locally before executing examples:
>
> - MySQL/MariaDB: `mysqladmin ping`
> - MongoDB: `mongosh --eval 'db.runCommand({ ping: 1 })'`
> - Redis: `redis-cli ping`

- Permission errors with MySQL imports: connect to the correct database or specify `-D <db>`.
- `Connection refused` in Mongo/Redis: check service status and host/port.

## Notes

- Big dataset files like `names.sql` are large and may not open well in all editors; load them directly via the MySQL client.
- Scripts are intentionally minimal to highlight the concept being practiced.

---

If you spot a doc issue or have an idea to make the exercises clearer, contributions are welcome. See `CONTRIBUTING.md`.
