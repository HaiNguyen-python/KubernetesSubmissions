from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import urllib.request

PORT = 8000
LOG_FILE_PATH = "/usr/src/app/files/log.txt"
# Địa chỉ của Ping Pong Service trong Cluster
PING_PONG_URL = "http://ping-pong-svc:5000/count"

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            
            # 1. Đọc timestamp & hash (vẫn đọc từ file nội bộ do Writer ghi)
            try:
                with open(LOG_FILE_PATH, "r") as f:
                    log_content = f.read().strip()
            except FileNotFoundError:
                log_content = "Waiting for logs..."

            # 2. Gọi HTTP sang Ping Pong để lấy số đếm
            try:
                response = urllib.request.urlopen(PING_PONG_URL)
                ping_content = response.read().decode()
            except Exception as e:
                ping_content = f"Error: {e}"
            
            # 3. Kết hợp hiển thị
            output = f"{log_content}\nPing / Pongs: {ping_content}"
            self.wfile.write(output.encode())
        else:
            self.send_response(404)

print(f"Reader started on port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), SimpleHandler).serve_forever()
