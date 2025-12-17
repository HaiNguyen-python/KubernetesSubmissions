from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import psycopg2

DB_PASS = os.getenv("POSTGRES_PASSWORD")

def get_db_connection():
    return psycopg2.connect(host="postgres-svc", database="postgres", user="postgres", password=DB_PASS)

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/todos":
            content_length = int(self.headers["Content-Length"])
            data = json.loads(self.rfile.read(content_length).decode())
            new_todo = data.get("todo", "")
            
            # LOGGING: Monitor every todo sent to the backend
            print(f"Received todo: {new_todo}", flush=True)

            # VALIDATION: Enforce 140 character limit
            if len(new_todo) > 140:
                print(f"REJECTED: Todo is too long ({len(new_todo)} characters)", flush=True)
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Todo is too long (max 140 characters)")
                return
            
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("INSERT INTO todos (content) VALUES (%s);", (new_todo,))
            conn.commit()
            cur.close()
            conn.close()
            self.send_response(200)
            self.end_headers()

    def do_GET(self):
        if self.path == "/todos":
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT content FROM todos;")
            todos = [row[0] for row in cur.fetchall()]
            cur.close()
            conn.close()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(todos).encode())

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
