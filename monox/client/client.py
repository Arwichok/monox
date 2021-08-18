from ..methods.request import MonoXRequest


class MonoXClient:

    def __init__(self, base_url: str, headers: dict[str, str]):
        self.base_url = base_url
        self.headers = headers

    def make_request(self, request: MonoXRequest):
        return NotImplemented

    def close(self):
        return NotImplemented
