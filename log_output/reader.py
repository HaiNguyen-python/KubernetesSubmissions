from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PORT = 8000
FILE_PATH = "/usr/src/app/files/log.txt"

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            try:
                with open(FILE_PATH, "r") as f:
                    content = f.read()
                self.wfile.write(content.encode())
            except FileNotFoundError:
                self.wfile.write(b"Waiting for logs...")
        else:
            self.send_response(404)

print(f"Reader started on port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), SimpleHandler).serve_forever()
