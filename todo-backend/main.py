from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

todos = ["Todo 1: Buy groceries", "Todo 2: Learn Kubernetes"]
# Lấy PORT từ biến môi trường, mặc định 8080
PORT = int(os.getenv("PORT", 8080))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/todos":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(todos).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/todos":
            try:
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode())
                new_todo = data.get("todo")
                if new_todo:
                    todos.append(new_todo)
                    self.send_response(200)
                else:
                    self.send_response(400)
            except:
                self.send_response(500)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

print(f"Todo Backend started on port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
