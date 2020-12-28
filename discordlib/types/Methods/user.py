from typing import Optional
from discordlib.types import User
from discordlib.types import AbstractResource
from discordlib.utils import get_request_data
from discordlib.types.objects import HTTPMethod, ME


class UserResource(AbstractResource):
    async def get_current(self) -> User:
        result = await self.request(HTTPMethod.GET, ME)
        return User(**result)

    async def get(self, user_id: int):
        result = await self.request(HTTPMethod.GET, user_id)
        return User(**result)

    async def modify_user(self, username: Optional[str] = None, avatar: Optional[str] = None):
        data = get_request_data(locals())
        result = await self.request(HTTPMethod.PATCH, ME, data=data)
        return User(**result)
