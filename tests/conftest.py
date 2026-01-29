"""Pytest configuration and fixtures."""

import pytest
import httpx


@pytest.fixture
def api_key() -> str:
    """Return a test API key."""
    return "test-api-key"


@pytest.fixture
def base_url() -> str:
    """Return a test base URL."""
    return "https://test.example.com"


@pytest.fixture
def mock_transport():
    """Create a mock transport for httpx."""

    class MockTransport(httpx.AsyncBaseTransport):
        def __init__(self, handler):
            self.handler = handler

        async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
            return self.handler(request)

    return MockTransport
