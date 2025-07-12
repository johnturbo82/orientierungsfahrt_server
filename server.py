from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

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
async def get_index() -> HTMLResponse:
    return HTMLResponse(content="<h1>Welcome to the Orientierungsfahrt Server</h1><p>Use the API to get information about the tours. See <a href='/docs'>Docs</a> for further information.</p>")

@app.get("/version")
async def get_version() -> int:
    return 1

@app.get("/tours")
async def get_tours() -> list[Turn]:
    t1 = Turn(id=1, name="Start", description="Start der Tour", image="start")
    t2 = Turn(id=2, name="Links abbiegen", description="Nach der Brücke", image="left")
    t2 = Turn(id=3, name="Rechts abbiegen", image="right")
    t3 = Turn(id=4, name="Ziel", description="Ende der Tour", image="end")
    return [t1, t2, t3]