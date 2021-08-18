from typing import Any

from pydantic import BaseModel

from .request import MonoXRequest
from ..models.model import MonoXModel


class MonoXMethod(BaseModel):

    def build_model(self, response_data: Any) -> MonoXModel:
        return NotImplemented

    def build_request(self) -> MonoXRequest:
        return NotImplemented
