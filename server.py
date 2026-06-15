#!/usr/bin/env python3
"""Run the Family Tree app locally or in Docker.

Local usage:
  python3 server.py
  open http://localhost:8000

Docker usage:
  docker build -t family-tree-app .
  docker run --rm -p 8000:8000 family-tree-app
"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
import webbrowser

PORT = int(os.environ.get("PORT", "8000"))
HOST = os.environ.get("HOST", "localhost")
OPEN_BROWSER = os.environ.get("OPEN_BROWSER", "1") == "1"
ROOT = Path(__file__).resolve().parent

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

if __name__ == "__main__":
    display_host = "localhost" if HOST in ("0.0.0.0", "::") else HOST
    url = f"http://{display_host}:{PORT}"
    print(f"Family Tree app running at {url}")
    print("Press Ctrl+C to stop.")
    if OPEN_BROWSER:
        try:
            webbrowser.open(url)
        except Exception:
            pass
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
