# MySQL advanced

Advanced SQL exercises showcasing schema design, triggers, stored procedures, scalar functions, views, indexing, and analytics queries.

## What’s inside

- Table design and constraints: `0-uniq_users.sql`, `1-country_users.sql`
- Analytics queries over datasets: `2-fans.sql`, `3-glam_rock.sql`
- Data integrity with triggers: `4-store.sql` (decrement stock on order), `5-valid_email.sql`
- Stored procedures: `6-bonus.sql` (ensure project, add bonus), `7-average_score.sql`
- Indexing: `8-index_my_names.sql`, `9-index_name_score.sql`
- Scalar function: `10-div.sql` (safe division)
- Views: `11-need_meeting.sql`
- Seeds and harness files: `7-init.sql`, `10-init.sql`, `11-init.sql`, `11-main.sql`
- Datasets: `metal_bands.sql`, `names.sql`

> [!NOTE]
> Some datasets are large (e.g., `names.sql`). Import them using the MySQL client instead of opening in your editor.

## Prerequisites

- MySQL 8.x or MariaDB 10.5+
- Access to a database/user you can use for testing

## Usage

1. (Optional) Create and use a scratch database

```
mysql -u <user> -p -e "CREATE DATABASE IF NOT EXISTS storage_lab;"
mysql -u <user> -p -D storage_lab -e "SELECT VERSION();"
```

2. Load datasets as needed

```
mysql -u <user> -p -D storage_lab < metal_bands.sql
mysql -u <user> -p -D storage_lab < names.sql
```

3. Run a task script

```
mysql -u <user> -p -D storage_lab < 3-glam_rock.sql
```

4. For tasks with init/main helpers

```
mysql -u <user> -p -D storage_lab < 11-init.sql
mysql -u <user> -p -D storage_lab < 11-need_meeting.sql
mysql -u <user> -p -D storage_lab < 11-main.sql
```

## Tips

- Use transactions while iterating on triggers/procedures so you can rollback easily.
- Prefer `IF NOT EXISTS`/`DROP … IF EXISTS` in experimental scripts.
- For partial indexes on strings, use prefix length like `name(1)` where supported.
