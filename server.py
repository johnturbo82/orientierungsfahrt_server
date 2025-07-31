from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from models import Turn
from images import images

app = FastAPI(title="Orientierungsfahrt Server", version="1.0")

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
    list_turns = []
    list_turns.append(Turn(id=1, name="Start", description="Start der Tour", image="cross_street"))
    list_turns.append(Turn(id=2, name="Links abbiegen", description="Nach der Brücke", image="left"))
    list_turns.append(Turn(id=3, name="Rechts abbiegen", image="right"))
    list_turns.append(Turn(id=4, name="Ziel", description="Ende der Tour", image="end"))
    return list_turns

@app.get("/images/{name}", response_model=tuple[str, str])
async def get_images(name: str) -> tuple[str, str]:
    return images.get(name, ""), images.get(f"{name}_dark", "")
