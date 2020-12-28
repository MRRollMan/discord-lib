from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    API_URL: str = None
    API_VERSION = None
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def request(self, method: str, path: str, data: dict) -> dict:
        pass
