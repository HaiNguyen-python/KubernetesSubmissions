from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import time
import urllib.request

PORT = 5000
# Thư mục lưu ảnh (sẽ được mount vào ổ cứng chung)
IMAGE_DIR = "/usr/src/app/files"
IMAGE_PATH = os.path.join(IMAGE_DIR, "image.jpg")
# URL lấy ảnh ngẫu nhiên
IMAGE_URL = "https://picsum.photos/1200"

# Đảm bảo thư mục tồn tại
os.makedirs(IMAGE_DIR, exist_ok=True)

def get_image():
    # Kiểm tra xem ảnh đã tồn tại chưa
    if os.path.exists(IMAGE_PATH):
        # Kiểm tra thời gian sửa đổi file
        file_age = time.time() - os.path.getmtime(IMAGE_PATH)
        if file_age < 3600: # 3600 giây = 60 phút (Hourly image)
            print("Image is cached. Serving local file.", flush=True)
            return

    # Nếu chưa có hoặc ảnh đã cũ > 60 phút -> Tải mới
    print("Downloading new image...", flush=True)
    try:
        urllib.request.urlretrieve(IMAGE_URL, IMAGE_PATH)
    except Exception as e:
        print(f"Failed to download image: {e}", flush=True)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Đảm bảo ảnh đã sẵn sàng trước khi hiện HTML
            get_image()
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            html = """
            <html>
            <body style="text-align:center;">
                <h1>The project App</h1>
                <img src="/image.jpg" style="max-width: 100%; height: auto;">
                <p>DevOps with Kubernetes</p>
                <form action="/" method="POST">
                    <input type="text" name="todo">
                    <input type="submit" value="Create TODO">
                </form>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
            
        elif self.path == "/image.jpg":
            # Phục vụ file ảnh
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

print(f"Server started on port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
