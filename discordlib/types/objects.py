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


class Guild(pydantic.BaseModel):
    id: int = None
    name: str = None
    icon: typing.Optional[str] = None
    icon_hash: typing.Optional[str] = None
    splash: typing.Optional[str] = None
    owner: typing.Optional[bool] = None
    owner_id: int = None
    permissions: typing.Optional[str] = None
    region: str = None
    afk_channel_id: typing.Optional[int] = None
    afk_timeout: int = None
    widget_enabled: typing.Optional[bool] = None
    widget_channel_id: typing.Optional[int] = None
    verification_level: int = None
    default_message_notifications: int = None
    explicit_content_filter: int = None
    roles: typing.List[dict] = None
    emojis: typing.List[dict] = None
    features: typing.List[dict] = None
    mfa_level: int = None
    application_id: typing.Optional[int] = None
    system_channel_id: typing.Optional[int] = None
    system_channel_flags: int = None
    rules_channel_id: typing.Optional[int] = None
    joined_at: typing.Optional[int] = None
    large: typing.Optional[bool] = None
    unavailable: typing.Optional[bool] = None
    member_count: typing.Optional[int] = None
    voice_states: typing.Optional[typing.List[dict]] = None
    members: typing.Optional[typing.List[dict]] = None
    channels: typing.Optional[typing.List[dict]] = None
    presences: typing.Optional[typing.List[dict]] = None
    max_presences: typing.Optional[int] = None
    max_members: typing.Optional[int] = None
    vanity_url_code: typing.Optional[str] = None
    description: typing.Optional[str] = None
    banner: typing.Optional[str] = None
    premium_tier: typing.Optional[int] = None
    premium_subscription_count: typing.Optional[int] = None
    preferred_locale: typing.Optional[str] = None
    public_updates_channel_id: typing.Optional[int] = None
    max_video_channel_users: typing.Optional[int] = None
    approximate_member_count: typing.Optional[int] = None
    approximate_presence_count: typing.Optional[int] = None
