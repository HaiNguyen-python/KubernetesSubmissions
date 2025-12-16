from http.server import HTTPServer, BaseHTTPRequestHandler

counter = 0

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global counter
        if self.path == "/pingpong":
            counter += 1
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"pong {counter}".encode())
        else:
            self.send_response(404)
            self.end_headers()

print("Ping Pong app started on port 5000", flush=True)
HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
