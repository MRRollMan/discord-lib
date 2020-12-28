import asyncio
from discordlib import API


async def main():
    api = API("TOKEN")
    me = await api.resources.user.get_current()
    print(f'{me.username}({me.id})')
    await api.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
