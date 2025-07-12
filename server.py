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

@app.get("/version", response_model=int)
async def get_version():
    return 1

@app.get("/tours", response_model=list[Turn])
async def get_tours():
    t1 = Turn(id=1, name="Start", description="Start der Tour", image="start")
    t2 = Turn(id=2, name="Links abbiegen", description="Nach der Brücke", image="left")
    t2 = Turn(id=2, name="Rechts abbiegen", image="right")
    t3 = Turn(id=3, name="Ziel", description="Ende der Tour", image="end")
    return [t1, t2, t3]