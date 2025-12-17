from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import time
import urllib.request
import urllib.parse
import json

PORT = 5000
IMAGE_DIR = "/usr/src/app/files"
IMAGE_PATH = os.path.join(IMAGE_DIR, "image.jpg")
IMAGE_URL = "https://picsum.photos/1200"

# Địa chỉ Backend (Tên Service trong K8s)
BACKEND_URL = "http://todo-backend-svc:2345/todos"

os.makedirs(IMAGE_DIR, exist_ok=True)

def get_image():
    if os.path.exists(IMAGE_PATH):
        file_age = time.time() - os.path.getmtime(IMAGE_PATH)
        if file_age < 3600:
            return
    try:
        urllib.request.urlretrieve(IMAGE_URL, IMAGE_PATH)
    except Exception as e:
        print(f"Failed to download image: {e}", flush=True)

def get_todos():
    try:
        response = urllib.request.urlopen(BACKEND_URL)
        data = json.loads(response.read().decode())
        return data
    except Exception as e:
        print(f"Error fetching todos: {e}", flush=True)
        return []

def create_todo(todo_text):
    try:
        data = json.dumps({"todo": todo_text}).encode("utf-8")
        req = urllib.request.Request(BACKEND_URL, data=data, headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req)
    except Exception as e:
        print(f"Error creating todo: {e}", flush=True)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            get_image()
            todos = get_todos()

            # Tạo danh sách HTML từ dữ liệu backend
            todo_list_html = ""
            for todo in todos:
                todo_list_html += f"<li>{todo}</li>"

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            html = f"""
            <html>
            <body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
                <h1>The project App</h1>
                <img src="/image.jpg" style="max-width: 400px; height: auto; border-radius: 10px;">

                <form action="/" method="POST" style="margin-top: 20px;">
                    <input type="text" name="todo" maxlength="140" placeholder="Enter a todo..." style="padding: 5px;">
                    <input type="submit" value="Create TODO" style="padding: 5px;">
                </form>

                <div style="margin-top: 20px; display: inline-block; text-align: left;">
                    <ul>
                        {todo_list_html}
                    </ul>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

        elif self.path == "/image.jpg":
            if os.path.exists(IMAGE_PATH):
                self.send_response(200)
                self.send_header("Content-type", "image/jpeg")
                self.end_headers()
                with open(IMAGE_PATH, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            # Parse form data (name=value)
            parsed_data = urllib.parse.parse_qs(post_data)
            todo_text = parsed_data.get("todo", [""])[0]

            if todo_text:
                create_todo(todo_text)

            # Refresh lại trang
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()

print(f"Server started on port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
