
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            status = 200
            response = {"status": "healthy"}
        else:
            status = 200
            response = {
                "message": "Hello from my DevOps project!",
                "application": "devops-demo",
                "version": os.getenv("APP_VERSION", "1.0.0")
            }

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(("0.0.0.0", 5000), AppHandler)
print("Application running on port 5000")
server.serve_forever()
