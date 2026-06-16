# Family Tree App

Runnable family tree editor with JSON, HTML, PDF and GEDCOM import/export.

## Run locally

```bash
python3 server.py
```

Open http://localhost:8000.

## Run with Docker

```bash
docker build -t family-tree-app .
docker run --rm -p 8000:8000 family-tree-app
```

Open http://localhost:8000.

## GEDCOM

Use **Import GEDCOM** to load `.ged` files. Use **Export GEDCOM** to download the current tree as `.ged`.
