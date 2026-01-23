from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/quantum-state")
async def get_state():
    return {
        "status": "OPERATIONAL",
        "infrastructure": [
            {"name": "Q-CORE-01", "status": "online"},
            {"name": "Q-CORE-02", "status": "online"},
            {"name": "WARP-GATE-01", "status": "online"},
            {"name": "TELEMETRY-ARRAY", "status": "online"},
            {"name": "CRYPTO-MESH", "status": "online"},
            {"name": "NEURAL-SYNC", "status": "online"}
        ],
        "latency": 15,
        "superposition": 99.1,
        "core_temp": 298.5,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "message": "Quantum Link Restored - OXYL.XYZ CORE ONLINE"
    }
