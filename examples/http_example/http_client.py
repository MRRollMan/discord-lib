import asyncio
from discordlib import ContextManager


async def main():
    context_manager = ContextManager(loop)
    async with context_manager as client:
        response = await client.request("GET", "https://google.com")
    await context_manager.close()
    print(response.status)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
