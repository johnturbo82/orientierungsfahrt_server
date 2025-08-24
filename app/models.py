from pydantic import BaseModel

class Turn(BaseModel):
    id: int
    order_num: int
    name: str
    description: str | None = None
    image: str | None = None