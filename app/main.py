from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from .database import get_image_by_title
from .models import Turn

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

@app.get("/version", response_model=int)
async def get_version() -> int:
    return 1

@app.get("/tours", response_model=list[Turn])
async def get_tours() -> list[Turn]:
    return get_tours()

@app.get("/images/{name}", response_model=tuple[str, str])
async def get_image(name: str) -> tuple[str, str]:
    return get_image_by_title(name), get_image_by_title(f"{name}_dark")
