from pydantic import BaseModel

class Turn(BaseModel):
    id: int
    name: str
    description: str | None = None