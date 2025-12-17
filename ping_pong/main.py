from http.server import HTTPServer, BaseHTTPRequestHandler

counter = 0

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global counter
        # Endpoint 1: /pingpong (Tăng số đếm và trả về cho người dùng)
        if self.path == "/pingpong":
            counter += 1
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"pong {counter}".encode())
        
        # Endpoint 2: /count (Chỉ trả về số đếm cho Log-Output app đọc)
        elif self.path == "/count":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(str(counter).encode())
            
        else:
            self.send_response(404)
            self.end_headers()

print("Ping Pong app started on port 5000", flush=True)
HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
