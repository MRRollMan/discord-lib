from abc import ABC, abstractmethod

from discordlib.http import AbstractHTTPClient


class AbstractContextManager(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @property
    @abstractmethod
    def http_client(self) -> AbstractHTTPClient:
        pass

    @abstractmethod
    async def close(self):
        pass

    async def __aenter__(self) -> AbstractHTTPClient:
        return self.http_client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
