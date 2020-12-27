from typing import Optional, NoReturn
from asyncio import AbstractEventLoop
from discordlib.http import AbstractHTTPClient, HTTPClient
from discordlib.http.context_manager import AbstractContextManager


class ContextManager(AbstractContextManager):
    def __init__(self, loop: Optional[AbstractEventLoop] = None, http_client: Optional[AbstractHTTPClient] = None):
        self._http_client = http_client or HTTPClient(loop)

    @property
    def http_client(self) -> AbstractHTTPClient:
        return self._http_client

    @http_client.setter
    def http_client(self, client) -> NoReturn:
        self._http_client = client

    async def close(self):
        await self.http_client.close()
