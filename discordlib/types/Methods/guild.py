import typing
from discordlib.types import Guild
from discordlib.types import AbstractResource
from discordlib.types.objects import HTTPMethod


class GuildResource(AbstractResource):
    async def get(self, guild_id: int) -> Guild:
        result = await self.request(HTTPMethod.GET, guild_id)
        return Guild(**result)

    async def get_channels(self, guild_id: int) -> Guild:
        result = await self.request(HTTPMethod.GET, f"{guild_id}/channels")
        return result
