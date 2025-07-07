from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Turn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get_tours():
    t1 = Turn(id=1, name="Start", description="Start der Tour")
    t2 = Turn(id=2, name="Station", description="Mach was!")
    t3 = Turn(id=3, name="Ziel", description="Ende der Tour")
    return [t1, t2, t3]