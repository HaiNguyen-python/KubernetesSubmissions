import time
import uuid
import datetime
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Global variable to store the UUID
random_string = str(uuid.uuid4())
port = 8000

# Function 1: Background thread to print logs every 5 seconds
def print_status():
    while True:
        timestamp = datetime.datetime.now().isoformat()
        print(f"{timestamp}: {random_string}", flush=True)
        time.sleep(5)

# Function 2: Web Server handler
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        timestamp = datetime.datetime.now().isoformat()
        # Respond with the same info
        response = f"{timestamp}: {random_string}"
        self.wfile.write(response.encode())

# Start the logging in a background thread
thread = threading.Thread(target=print_status)
thread.daemon = True
thread.start()

# Start the Web Server in the main thread
print(f"Server started in port {port}", flush=True)
httpd = HTTPServer(("0.0.0.0", port), SimpleHandler)
httpd.serve_forever()
