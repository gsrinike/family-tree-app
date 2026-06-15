# Family Tree App Docker image
# Builds a lightweight container that serves the static HTML app on port 8000.
FROM python:3.12-slim

WORKDIR /app

# Copy app files
COPY index.html family-tree.json server.py README.md ./

# The app is static. server.py serves files using Python's built-in HTTP server.
EXPOSE 8000

ENV HOST=0.0.0.0
ENV PORT=8000
ENV OPEN_BROWSER=0

CMD ["python", "server.py"]
