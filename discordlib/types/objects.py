import typing
from enum import Enum

import pydantic

ME = "@me"


class HTTPMethod:
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"


class PremiumTypes(Enum):
    NONE = 0
    NITRO_CLASSIC = 1
    NITRO = 2


class UserFlags(Enum):
    NONE = 0
    DISCORD_EMPLOYEE = 1 << 0
    PARTNERED_SERVER_OWNER = 1 << 1
    HYPERSQUAD__EVENTS = 1 << 2
    BUG_HUNTER_LEVEL_1 = 1 << 3
    HOUSE_BRAVERY = 1 << 6
    HOUSE_BRILLIANCE = 1 << 7
    HOUSE_BALANCE = 1 << 8
    EARLY_SUPPORTER = 1 << 9
    TEAM_USER = 1 << 10
    SYSTEM = 1 << 12
    BUG_HUNTER_LEVEL_2 = 1 << 14
    VERIFIED_BOT = 1 << 16
    EARLY_VERIFIED_BOT_DEVELOPER = 1 << 17


class User(pydantic.BaseModel):
    id: int = None
    username: str = None
    discriminator: str = None
    avatar: str = None
    bot: typing.Optional[bool] = None
    system: typing.Optional[bool] = None
    mfa_enabled: typing.Optional[bool] = None
    locale: typing.Optional[str] = None
    verified: typing.Optional[bool] = None
    email: typing.Optional[str] = None
    flags: typing.Optional[UserFlags]
    premium_type: typing.Optional[PremiumTypes]
    public_flags: typing.Optional[UserFlags]
