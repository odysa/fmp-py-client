"""Tests for the exceptions module."""

from fmp_py_client._exceptions import (
    FMPError,
    FMPAPIError,
    FMPAuthenticationError,
    FMPRateLimitError,
    FMPNotFoundError,
    FMPConnectionError,
    FMPTimeoutError,
)


class TestFMPError:
    """Tests for FMPError base class."""

    def test_init_with_message(self):
        """Test initialization with message."""
        error = FMPError("Test error message")

        assert error.message == "Test error message"
        assert str(error) == "Test error message"

    def test_inheritance(self):
        """Test that FMPError inherits from Exception."""
        error = FMPError("Test")

        assert isinstance(error, Exception)


class TestFMPAPIError:
    """Tests for FMPAPIError class."""

    def test_init_with_required_params(self):
        """Test initialization with required params."""
        error = FMPAPIError("API error", status_code=500)

        assert error.message == "API error"
        assert error.status_code == 500
        assert error.response_body is None

    def test_init_with_response_body(self):
        """Test initialization with response body."""
        error = FMPAPIError(
            "API error",
            status_code=500,
            response_body='{"error": "Internal error"}',
        )

        assert error.response_body == '{"error": "Internal error"}'

    def test_inheritance(self):
        """Test that FMPAPIError inherits from FMPError."""
        error = FMPAPIError("Test", status_code=400)

        assert isinstance(error, FMPError)
        assert isinstance(error, Exception)


class TestFMPAuthenticationError:
    """Tests for FMPAuthenticationError class."""

    def test_init(self):
        """Test initialization."""
        error = FMPAuthenticationError(
            "Invalid API key",
            status_code=401,
            response_body="Unauthorized",
        )

        assert error.message == "Invalid API key"
        assert error.status_code == 401
        assert error.response_body == "Unauthorized"

    def test_inheritance(self):
        """Test that FMPAuthenticationError inherits from FMPAPIError."""
        error = FMPAuthenticationError("Test", status_code=401)

        assert isinstance(error, FMPAPIError)
        assert isinstance(error, FMPError)


class TestFMPRateLimitError:
    """Tests for FMPRateLimitError class."""

    def test_init_with_defaults(self):
        """Test initialization with defaults."""
        error = FMPRateLimitError("Rate limit exceeded")

        assert error.message == "Rate limit exceeded"
        assert error.status_code == 429
        assert error.retry_after is None
        assert error.response_body is None

    def test_init_with_retry_after(self):
        """Test initialization with retry_after."""
        error = FMPRateLimitError(
            "Rate limit exceeded",
            retry_after=60.0,
            response_body="Too many requests",
        )

        assert error.retry_after == 60.0
        assert error.response_body == "Too many requests"

    def test_init_with_custom_status_code(self):
        """Test initialization with custom status code."""
        error = FMPRateLimitError("Rate limit", status_code=503)

        assert error.status_code == 503

    def test_inheritance(self):
        """Test that FMPRateLimitError inherits from FMPAPIError."""
        error = FMPRateLimitError("Test")

        assert isinstance(error, FMPAPIError)
        assert isinstance(error, FMPError)


class TestFMPNotFoundError:
    """Tests for FMPNotFoundError class."""

    def test_init(self):
        """Test initialization."""
        error = FMPNotFoundError(
            "Resource not found",
            status_code=404,
            response_body="Not found",
        )

        assert error.message == "Resource not found"
        assert error.status_code == 404
        assert error.response_body == "Not found"

    def test_inheritance(self):
        """Test that FMPNotFoundError inherits from FMPAPIError."""
        error = FMPNotFoundError("Test", status_code=404)

        assert isinstance(error, FMPAPIError)
        assert isinstance(error, FMPError)


class TestFMPConnectionError:
    """Tests for FMPConnectionError class."""

    def test_init(self):
        """Test initialization."""
        error = FMPConnectionError("Connection refused")

        assert error.message == "Connection refused"

    def test_inheritance(self):
        """Test that FMPConnectionError inherits from FMPError."""
        error = FMPConnectionError("Test")

        assert isinstance(error, FMPError)
        assert isinstance(error, Exception)

    def test_does_not_have_status_code(self):
        """Test that FMPConnectionError does not have status_code."""
        error = FMPConnectionError("Test")

        assert not hasattr(error, "status_code")


class TestFMPTimeoutError:
    """Tests for FMPTimeoutError class."""

    def test_init(self):
        """Test initialization."""
        error = FMPTimeoutError("Request timed out")

        assert error.message == "Request timed out"

    def test_inheritance(self):
        """Test that FMPTimeoutError inherits from FMPError."""
        error = FMPTimeoutError("Test")

        assert isinstance(error, FMPError)
        assert isinstance(error, Exception)

    def test_does_not_have_status_code(self):
        """Test that FMPTimeoutError does not have status_code."""
        error = FMPTimeoutError("Test")

        assert not hasattr(error, "status_code")
