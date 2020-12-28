from typing import Optional

from discordlib import ContextManager
from discordlib import HTTPClient
from discordlib.api import AbstractAPI
from discordlib.utils import generate_user_agent


class API(AbstractAPI):
    _api_version: int = 7
    _api_url: str = 'https://discord.com/api/v{0}/'

    def __init__(
            self,
            bot_token: str,
            api_version: Optional[int] = None,
            user_agent: Optional[str] = None,
            context_manager: Optional[ContextManager] = None
    ):
        self._bot_token = f"Bot {bot_token}"
        self._user_agent = user_agent or generate_user_agent('DiscordBot')
        if api_version:
            self._api_version = api_version
        self._api_url = self._api_url.format(self._api_version)
        self._http_client = HTTPClient(headers={"Authorization": self._bot_token, "User-Agent": self._user_agent})
        self.http = context_manager or ContextManager(http_client=self._http_client)

    async def request(self, method: str, path: str, data: dict = None) -> dict:
        async with self.http as session:
            response = await session.request_json(
                method=method,
                url=self._api_url + path,
                data=data
            )
        return response
