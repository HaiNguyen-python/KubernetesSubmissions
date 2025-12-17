from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import psycopg2

# 1. Get database password from Secret environment variable
DB_PASS = os.getenv("POSTGRES_PASSWORD")
PORT = int(os.getenv("PORT", 8080))

def get_db_connection():
    # Connects to the headless service "postgres-svc"
    return psycopg2.connect(host="postgres-svc", database="postgres", user="postgres", password=DB_PASS)

def init_db():
    # Initialize the database table
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS todos (id serial PRIMARY KEY, content text);")
    conn.commit()
    cur.close()
    conn.close()

# Initialize DB on startup
try:
    init_db()
except Exception as e:
    print(f"Waiting for DB... Error: {e}", flush=True)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/todos":
            conn = get_db_connection()
            cur = conn.cursor()
            # Fetch todos from database
            cur.execute("SELECT content FROM todos;")
            todos = [row[0] for row in cur.fetchall()]
            cur.close()
            conn.close()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(todos).encode())

    def do_POST(self):
        if self.path == "/todos":
            content_length = int(self.headers["Content-Length"])
            data = json.loads(self.rfile.read(content_length).decode())
            new_todo = data.get("todo")
            
            if new_todo:
                conn = get_db_connection()
                cur = conn.cursor()
                # Insert new todo into database
                cur.execute("INSERT INTO todos (content) VALUES (%s);", (new_todo,))
                conn.commit()
                cur.close()
                conn.close()
                self.send_response(200)
            else:
                self.send_response(400)
            self.end_headers()

print(f"Backend started on port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
