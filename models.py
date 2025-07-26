from pydantic import BaseModel

class Turn(BaseModel):
    id: int
    name: str
    description: str | None = None
    image: str | None = None
    image_source: str | None = None