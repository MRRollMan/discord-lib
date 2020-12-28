from abc import ABC
from typing import Optional
from discordlib.api import AbstractAPI


class AbstractResource(ABC):
    def __init__(self, resource_name: str, api: AbstractAPI):
        self.resource_name = resource_name
        self.__api = api

    async def request(self, method: str, path: str, data: Optional[dict] = None):
        return await self.__api.request(method, self.resource_name + f"{path}", data)