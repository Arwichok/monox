from typing import List

from .method import MonoXMethod
from .request import MonoXRequest
from ..models.currency import Currency


class GetCurrency(MonoXMethod):

    def build_model(self, response_data: List) -> List[Currency]:
        return [Currency(**d) for d in response_data]

    def build_request(self):
        return MonoXRequest(
            method="GET",
            path="/bank/currency"
        )
