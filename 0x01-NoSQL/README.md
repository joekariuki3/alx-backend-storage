# NoSQL (MongoDB)

MongoDB exercises with two parts:

- Shell snippets (`0`–`7`) to practice basic CRUD and filters
- Python helpers (`8`–`11`) using PyMongo to list, insert, update topics, and query by topic

## Prerequisites

- MongoDB Community Server running locally (`mongodb://127.0.0.1:27017`)
- Python 3.8+
- Packages: `pymongo` (install via repo-level `requirements.txt`)

## Shell snippets

Run directly with `mongosh`:

```
mongosh < 0-list_databases
mongosh < 1-use_or_create_database
mongosh < 2-insert
mongosh < 3-all
mongosh < 4-match
mongosh < 5-count
mongosh < 6-update
mongosh < 7-delete
```

> [!TIP]
> The snippets assume database `my_db` and collection `school` for consistency across tasks.

## Python helpers and demos

Files:

- `8-all.py`: list all documents in a collection
- `9-insert_school.py`: insert a document from kwargs and return the inserted id
- `10-update_topics.py`: update a school’s topics by name (multi-update)
- `11-schools_by_topic.py`: find schools by topic

Run the included demo scripts while MongoDB is running:

```
python 8-main.py
python 9-main.py
python 10-main.py
python 11-main.py
```

## Notes

- Connection string is hard-coded to localhost; adjust if you’re running MongoDB elsewhere.
- Use appropriate indexes (`name`, `topics`) for larger datasets to keep queries fast.
