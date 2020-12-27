import asyncio
from typing import Optional, NoReturn

from aiohttp import ClientSession, TCPConnector, ClientResponse

from discordlib.http import AbstractHTTPClient


class HTTPClient(AbstractHTTPClient):
    def __init__(
            self,
            loop: Optional[asyncio.AbstractEventLoop] = None,
            session: Optional[ClientSession] = None,
            verify_ssl: Optional[bool] = True,
            headers: Optional[dict] = None,
            **kwargs
    ):
        self.loop = loop or asyncio.get_event_loop()
        self.session = session or ClientSession(
            connector=TCPConnector(verify_ssl=verify_ssl, loop=self.loop),
            loop=self.loop,
            headers=headers,
            **kwargs
        )

    async def request_text(self, method: str, url: str, data: Optional[dict] = None, **kwargs) -> str:
        async with self.session.request(method=method, url=url, data=data, **kwargs) as response:
            return await response.text()

    async def request_json(self, method: str, url: str, data: Optional[dict] = None, **kwargs) -> dict:
        async with self.session.request(method=method, url=url, data=data, **kwargs) as response:
            return await response.json()

    async def request_bytes(self, method: str, url: str, data: Optional[dict] = None, **kwargs) -> bytes:
        async with self.session.request(method=method, url=url, data=data, **kwargs) as response:
            return await response.read()

    async def request(self, method: str, url: str, data: Optional[dict] = None, **kwargs) -> ClientResponse:
        return await self.session.request(method=method, url=url, data=data, **kwargs)

    async def close(self) -> NoReturn:
        await self.session.close()
