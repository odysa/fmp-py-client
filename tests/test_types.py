"""Tests for the types module."""

from fmp_py_client._types import Period, Timeframe


class TestPeriod:
    """Tests for Period enum."""

    def test_annual_value(self):
        """Test ANNUAL value."""
        assert Period.ANNUAL == "annual"
        assert Period.ANNUAL.value == "annual"

    def test_quarter_value(self):
        """Test QUARTER value."""
        assert Period.QUARTER == "quarter"
        assert Period.QUARTER.value == "quarter"

    def test_str_enum_behavior(self):
        """Test that Period works as a string."""
        assert str(Period.ANNUAL) == "annual"
        assert str(Period.QUARTER) == "quarter"

    def test_comparison_with_string(self):
        """Test comparison with strings."""
        assert Period.ANNUAL == "annual"
        assert Period.QUARTER == "quarter"

    def test_all_members(self):
        """Test that all expected members exist."""
        members = list(Period)

        assert len(members) == 2
        assert Period.ANNUAL in members
        assert Period.QUARTER in members


class TestTimeframe:
    """Tests for Timeframe enum."""

    def test_one_min_value(self):
        """Test ONE_MIN value."""
        assert Timeframe.ONE_MIN == "1min"
        assert Timeframe.ONE_MIN.value == "1min"

    def test_five_min_value(self):
        """Test FIVE_MIN value."""
        assert Timeframe.FIVE_MIN == "5min"

    def test_fifteen_min_value(self):
        """Test FIFTEEN_MIN value."""
        assert Timeframe.FIFTEEN_MIN == "15min"

    def test_thirty_min_value(self):
        """Test THIRTY_MIN value."""
        assert Timeframe.THIRTY_MIN == "30min"

    def test_one_hour_value(self):
        """Test ONE_HOUR value."""
        assert Timeframe.ONE_HOUR == "1hour"

    def test_four_hour_value(self):
        """Test FOUR_HOUR value."""
        assert Timeframe.FOUR_HOUR == "4hour"

    def test_one_day_value(self):
        """Test ONE_DAY value."""
        assert Timeframe.ONE_DAY == "1day"

    def test_str_enum_behavior(self):
        """Test that Timeframe works as a string."""
        assert str(Timeframe.ONE_MIN) == "1min"
        assert str(Timeframe.ONE_DAY) == "1day"

    def test_comparison_with_string(self):
        """Test comparison with strings."""
        assert Timeframe.ONE_MIN == "1min"
        assert Timeframe.ONE_DAY == "1day"

    def test_all_members(self):
        """Test that all expected members exist."""
        members = list(Timeframe)

        assert len(members) == 7
        assert Timeframe.ONE_MIN in members
        assert Timeframe.FIVE_MIN in members
        assert Timeframe.FIFTEEN_MIN in members
        assert Timeframe.THIRTY_MIN in members
        assert Timeframe.ONE_HOUR in members
        assert Timeframe.FOUR_HOUR in members
        assert Timeframe.ONE_DAY in members
