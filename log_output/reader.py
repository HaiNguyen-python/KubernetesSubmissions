from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import urllib.request

PORT = 8000
LOG_FILE_PATH = "/usr/src/app/files/log.txt"
PING_PONG_URL = "http://ping-pong-svc:5000/count"
CONFIG_FILE_PATH = "/usr/src/app/config/information.txt" # Đường dẫn mount file

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

            # 2. Gọi Ping Pong
            try:
                response = urllib.request.urlopen(PING_PONG_URL)
                ping_content = response.read().decode()
            except Exception as e:
                ping_content = f"Error: {e}"
            
            # 3. Đọc ConfigMap (Bài 2.5)
            # - Biến môi trường
            message_env = os.getenv("MESSAGE", "No message")
            
            # - File content
            try:
                with open(CONFIG_FILE_PATH, "r") as f:
                    file_content = f.read().strip()
            except FileNotFoundError:
                file_content = "File not found"

            # 4. Hiển thị
            output = f"file content: {file_content}\nenv variable: MESSAGE={message_env}\n{log_content}\nPing / Pongs: {ping_content}"
            self.wfile.write(output.encode())
        else:
            self.send_response(404)

print(f"Reader started on port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), SimpleHandler).serve_forever()
