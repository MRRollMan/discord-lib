import pytest

from sys import version_info as py_ver
from http import HTTPStatus

from aiohttp import __version__ as aiohttpver

from discordlib import HTTPClient
from discordlib import ContextManager
from discordlib import __version__ as discordlibver


@pytest.mark.asyncio
async def test_http_request():
    client = HTTPClient()
    response = await client.request('GET', f'https://httpbin.org/status/{HTTPStatus.NOT_FOUND}')
    await client.close()
    assert response.status == HTTPStatus.NOT_FOUND


@pytest.mark.asyncio
async def test_user_agent_http():
    user_agent = f'TestRequest (discordlib/{discordlibver}) Python/{py_ver[0]}.{py_ver[1]} aiohttp/{aiohttpver}'
    client = HTTPClient(headers={'User-Agent': user_agent})
    response = await client.request_json('GET', 'https://httpbin.org/user-agent')
    await client.close()
    assert response['user-agent'] == user_agent


@pytest.mark.asyncio
async def test_client_manager():
    context_manager = ContextManager()
    async with context_manager as client:
        assert (await client.request("GET", "https://example.com")).status == HTTPStatus.OK
