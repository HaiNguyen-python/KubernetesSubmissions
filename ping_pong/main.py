import psycopg2
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

# Connection config - Using the Headless Service name "postgres-svc"
DB_HOST = "postgres-svc"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "pass123"

def get_db_connection():
    # Establishes connection to the PostgreSQL instance
    return psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)

def init_db():
    # Creates table and initial row if they do not exist
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS pings (id serial PRIMARY KEY, count integer);")
    cur.execute("SELECT count FROM pings WHERE id = 1;")
    if cur.fetchone() is None:
        cur.execute("INSERT INTO pings (id, count) VALUES (1, 0);")
    conn.commit()
    cur.close()
    conn.close()

# Initialize DB structure on startup
try:
    init_db()
except Exception as e:
    print(f"Waiting for database... Error: {e}", flush=True)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/pingpong" or self.path == "/count":
            conn = get_db_connection()
            cur = conn.cursor()
            
            if self.path == "/pingpong":
                # Atomically increment the counter in the database
                cur.execute("UPDATE pings SET count = count + 1 WHERE id = 1 RETURNING count;")
                count = cur.fetchone()[0]
                conn.commit()
                response = f"pong {count}"
            else:
                # Fetch only for Log-output app request
                cur.execute("SELECT count FROM pings WHERE id = 1;")
                count = cur.fetchone()[0]
                response = str(count)
                
            cur.close()
            conn.close()
            
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(response.encode())

print("Ping Pong app started with Postgres backend", flush=True)
HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
