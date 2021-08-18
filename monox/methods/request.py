from pydantic import BaseModel


class MonoXRequest(BaseModel):
    method: str = "GET"
    path: str = "/"
    headers: dict[str, str] = {}
