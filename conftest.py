from playwright.async_api import async_playwright
import pytest
import asyncio


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="class")
async def aplaywright():
    async with async_playwright() as pw:
        yield pw