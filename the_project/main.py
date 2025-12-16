import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Get the PORT from environment variables, default to 5000 if not set
port = int(os.environ.get('PORT', 5000))

# Print the startup message as required by the exercise
print(f"Server started in port {port}", flush=True)

# Create and start the HTTP server
httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
httpd.serve_forever()