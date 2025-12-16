from http.server import HTTPServer, BaseHTTPRequestHandler
import os

FILE_PATH = "/usr/src/app/data/pingpong.txt"

# Ensure directory exists
os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

def get_counter():
    try:
        with open(FILE_PATH, "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0

def save_counter(count):
    with open(FILE_PATH, "w") as f:
        f.write(str(count))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/pingpong":
            counter = get_counter()
            counter += 1
            save_counter(counter)
            
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"pong {counter}".encode())
        else:
            self.send_response(404)
            self.end_headers()

print("Ping Pong app started on port 5000", flush=True)
HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
