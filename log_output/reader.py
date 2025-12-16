from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PORT = 8000
LOG_FILE_PATH = "/usr/src/app/files/log.txt"
PING_PONG_FILE_PATH = "/usr/src/app/data/pingpong.txt"

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            
            # 1. Đọc timestamp & hash
            try:
                with open(LOG_FILE_PATH, "r") as f:
                    log_content = f.read().strip()
            except FileNotFoundError:
                log_content = "Waiting for logs..."

            # 2. Đọc ping pong counter
            try:
                with open(PING_PONG_FILE_PATH, "r") as f:
                    ping_content = f.read().strip()
            except FileNotFoundError:
                ping_content = "0"
            
            # 3. Kết hợp hiển thị
            output = f"{log_content}\nPing / Pongs: {ping_content}"
            self.wfile.write(output.encode())
        else:
            self.send_response(404)

print(f"Reader started on port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), SimpleHandler).serve_forever()
