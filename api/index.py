from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {"status": "BEAST IS ALIVE", "message": "No more sickness"}
        self.wfile.write(json.dumps(data).encode())
