import asyncio
from discordlib import API


async def main():
    api = API("TOKEN")
    me = await api.request("GET", "/users/@me")
    print(me)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())