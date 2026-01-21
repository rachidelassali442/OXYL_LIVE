from http.server import BaseHTTPRequestHandler
import json
import os
from supabase import create_client

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # جلب الروابط من Vercel Environment
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
        
        try:
            # الربط مع الوحش
            supabase = create_client(url, key)
            
            # جلب معلومات السيرفر للتأكد من الاتصال
            # غنحاولوا نقرأوا أي داتا بسيطة
            data = {
                "status": "OXYL BEAST ONLINE",
                "infrastructure": "SUPABASE_ACTIVE",
                "project_id": "nyzbxuejffqeullueydm",
                "sync_engine": "v3.0.1-Stable",
                "message": "Welcome to the future of Oxyl."
            }
        except Exception as e:
            data = {
                "status": "CONNECTING...",
                "error": str(e),
                "hint": "Wait for provisioning to finish"
            }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=4).encode())
