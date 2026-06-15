# Family Tree App

This is a runnable local web app built from your existing HTML family-tree editor.

## Run locally

1. Install Python 3 if it is not already installed.
2. Open a terminal in this folder.
3. Run:

```bash
python3 server.py
```

On Windows, use:

```bash
py server.py
```

4. Open `http://localhost:8000` in Chrome or Edge.

## Run with Docker

Build the Docker image:

```bash
docker build -t family-tree-app .
```

Run the container:

```bash
docker run --rm -p 8000:8000 family-tree-app
```

Open:

```text
http://localhost:8000
```

Optional: run with a custom port on your computer:

```bash
docker run --rm -p 8080:8000 family-tree-app
```

Then open `http://localhost:8080`.

## Files

- `index.html` — the app UI and editor logic.
- `family-tree.json` — your current tree data, loaded automatically on first run.
- `server.py` — a tiny local web server.

## Notes

- The app saves edits in your browser using IndexedDB/localStorage.
- The **Save Tree** button can also save to a chosen folder in Chrome/Edge using the File System Access API.
- Export JSON/HTML/PDF are available from the toolbar.
- PDF export uses the online `html2pdf.js` CDN already present in the HTML, so internet access is needed for PDF export unless that library is bundled locally later.
