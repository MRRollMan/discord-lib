from discordlib.types.Methods import UserResource


class Resources:
    def __init__(self, api):
        self.user = UserResource("/users/", api)
