from discordlib.types.Methods import UserResource
from discordlib.types.Methods import GuildResource


class Resources:
    def __init__(self, api):
        self.user = UserResource("/users/", api)
        self.guild = GuildResource("/guilds/", api)
