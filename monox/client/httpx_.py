from httpx import AsyncClient

from .client import MonoXClient
from ..errors import TooManyRequests
from ..methods.request import MonoXRequest


class HttpxClient(MonoXClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = AsyncClient()

    async def make_request(self, request: MonoXRequest):
        response = await self.client.request(
            method=request.method,
            url=self.base_url + request.path,
            headers=self.headers.update(request.headers)
        )
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            raise TooManyRequests
        else:
            raise Exception(response.status_code, response.json().get("errorDescription"))

    async def close(self):
        await self.client.aclose()
