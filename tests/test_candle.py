from datetime import UTC, datetime
from decimal import Decimal

from app.domain.candle import Candle


def test_candle_stores_fields() -> None:
    timestamp = datetime(2026, 10, 1, 20, 0, tzinfo=UTC)
    candle = Candle(
        timestamp=timestamp,
        open=Decimal("10.00"),
        high=Decimal("12.00"),
        low=Decimal("9.50"),
        close=Decimal("11.00"),
        volume=Decimal("1500.50"),
    )
    assert candle.timestamp == timestamp
    assert candle.open == Decimal("10.00")
    assert candle.high == Decimal("12.00")
    assert candle.low == Decimal("9.50")
    assert candle.close == Decimal("11.00")
    assert candle.volume == Decimal("1500.50")
