from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
        "message": "OXYL.XYZ CORE ONLINE"
    }

@app.get("/")
async def root():
    return {"message": "OXYL API ACTIVE"}
