from typing import Optional

from pydantic import Field

from ..models.model import MonoXModel


class Currency(MonoXModel):
    a: int = Field(None, alias="currencyCodeA")
    b: int = Field(None, alias="currencyCodeB")
    date: int
    sell: Optional[float] = Field(None, alias="rateSell")
    buy: Optional[float] = Field(None, alias="rateBuy")
    cross: Optional[float] = Field(None, alias="rateCross")
