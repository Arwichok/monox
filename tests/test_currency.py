import json

import httpx
import pytest
import respx

from monox import MonoX, Currency


@respx.mock
@pytest.mark.asyncio
async def test_currency():
    def_cur = Currency(currencyCodeA=34, currencyCodeB=22, date=45454545, rateBuy=25.33)

    respx.get("https://api.monobank.ua/bank/currency")\
         .mock(return_value=httpx.Response(200, json=[def_cur.dict(by_alias=True)]))

    async with MonoX() as m:
        cur = await m.currency()
        await m.currency()
        assert cur == [def_cur]

