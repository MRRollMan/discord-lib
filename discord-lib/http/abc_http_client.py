from typing import Optional, NoReturn

from abc import ABC, abstractmethod

from aiohttp import ClientResponse


class AbstractHTTPClient(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    async def request_text(self, method: str, url: str, data: Optional[dict] = None, **kwargs) -> str:
        pass

    @abstractmethod
    async def request_json(self, method: str, url: str, data: Optional[dict] = None, **kwargs) -> dict:
        pass

    @abstractmethod
    async def request_bytes(self, method: str, url: str, data: Optional[dict] = None, **kwargs) -> bytes:
        pass

    @abstractmethod
    async def request(self, method: str, url: str, **kwargs) -> ClientResponse:
        pass

    @abstractmethod
    async def close(self) -> NoReturn:
        pass
