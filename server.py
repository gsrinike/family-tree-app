from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    print("Family Tree app running at http://localhost:8000")
    server.serve_forever()
