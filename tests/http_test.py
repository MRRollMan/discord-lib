import sys
import pytest
from aiohttp import __version__ as aioversion

from discordlib import HTTPClient
from discordlib import ClientManager
from discordlib import __version__ as dslibversion

py_version = sys.version_info


@pytest.mark.asyncio
async def test_http_request():
    client = HTTPClient()
    response = await client.request('GET', 'https://httpbin.org/status/404')
    await client.close()
    assert response.status == 404


@pytest.mark.asyncio
async def test_user_agent_http():
    user_agent = f'TestRequest (discordlib/{dslibversion}) Python/{py_version[0]}.{py_version[1]} aiohttp/{aioversion}'
    client = HTTPClient(headers={'User-Agent': user_agent})
    response = await client.request_json('GET', 'https://httpbin.org/user-agent')
    await client.close()
    assert response['user-agent'] == user_agent


@pytest.mark.asyncio
async def test_client_manager():
    client_manager = ClientManager()
    async with client_manager as client:
        assert (await client.request("GET", "https://example.com")).status == 200