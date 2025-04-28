import pytest
import asyncio

@pytest.fixture(scope="session")
def event_loop():
    """Create and cleanup event loop"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()
    asyncio.set_event_loop(None)

@pytest.fixture(autouse=True)
async def cleanup_discord():
    """Cleanup discord client after tests"""
    from bot import client
    yield
    if not client.is_closed():
        await client.close()