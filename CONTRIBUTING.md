# Contributing

Thanks for your interest in improving this repository! The project is split into three independent sub-projects (MySQL, MongoDB, Redis). Please keep changes scoped and tested per sub-project when possible.

## Getting started

- Use Python 3.8+ and install dependencies from `requirements.txt`.
- Ensure you have local instances of MySQL/MariaDB, MongoDB, and Redis as needed for your change.
- Prefer small, focused pull requests with clear descriptions.

## Coding guidelines

- Python
  - Follow PEP 8 style conventions.
  - Keep modules self-contained and minimal; avoid introducing heavy dependencies.
- SQL
  - Write idempotent scripts where practical (`IF EXISTS`/`IF NOT EXISTS`).
  - Include `DELIMITER` guards around triggers/procedures/functions when needed.
- Shell/mongo scripts
  - Keep scripts concise and comment intent at the top.

## Commit messages

Use clear, imperative commit messages. Conventional Commits are welcome:

- `feat(mysql): add trigger to decrement stock`
- `fix(nosql): correct query filter for topics`
- `docs(redis): clarify cache TTL`

## Pull request checklist

- [ ] Change is focused to a single sub-project or clearly separated by folders
- [ ] Docs updated (READMEs, comments) if behavior or usage changed
- [ ] Tested locally against the relevant datastore(s)

## Reporting issues

Please include:

- Sub-project path (e.g., `0x02-redis_basic`)
- Expected vs actual behavior
- Steps to reproduce and environment details (OS, versions)
