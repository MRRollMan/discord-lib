import asyncio
from discordlib import ContextManager
from discordlib import HTTPClient


async def main():
    http = HTTPClient(headers={"User-Agent": "HTTP Example"})
    context_manager = ContextManager(http_client=http)
    async with context_manager as client:
        response = await client.request_json("GET", "https://httpbin.org/user-agent")
    await context_manager.close()
    print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
