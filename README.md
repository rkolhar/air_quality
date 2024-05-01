## Air quality measurement

This repo extracts measurement data from OpenAQ API, transforms and loads data into postgres database using a pydantic model.

## How to run:
1. Spin up docker containers using cmd:
```bash
    docker compose up –d –build
```

2. Check data in postgres db
```bash
    psql -U postgres -d postgres
```
3. Execute queries from queries.sql 
