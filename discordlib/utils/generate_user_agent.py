from sys import version_info as py_ver
import aiohttp
import discordlib


def generate_user_agent(name):
    return f'{name} (discordlib/{discordlib.__version__}) Python/{py_ver[0]}.{py_ver[1]} aiohttp/{aiohttp.__version__}'
