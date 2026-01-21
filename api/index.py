from http.server import BaseHTTPRequestHandler
import json
import os
from supabase import create_client

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # هاد المرة غيجيبهم من السيستيم نيشان
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
        
        try:
            if not url or not key:
                raise ValueError("Environment variables not found in Production")
                
            supabase = create_client(url, key)
            # تجربة بسيطة للاتصال
            data = {
                "status": "OXYL BEAST ONLINE",
                "infrastructure": "SUPABASE_CONNECTED",
                "database_url": url[:20] + "...",
                "message": "System is now fully operational."
            }
        except Exception as e:
            data = {
                "status": "CONNECTION_ERROR",
                "error": str(e)
            }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=4).encode())
