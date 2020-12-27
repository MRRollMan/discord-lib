from typing import Optional, NoReturn
from discordlib.http import AbstractHTTPClient, HTTPClient
from discordlib.http.client_manager.abc_client_manager import AbstractClientManager


class ClientManager(AbstractClientManager):
    def __init__(self, http_client: Optional[AbstractHTTPClient] = None):
        self._http_client = http_client or HTTPClient()

    @property
    def http_client(self) -> AbstractHTTPClient:
        return self._http_client

    @http_client.setter
    def http_client(self, client) -> NoReturn:
        self._http_client = client

    async def close(self):
        await self.http_client.close()
