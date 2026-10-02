from datetime import UTC, datetime
from decimal import Decimal

import pytest

from app.domain.candle import Candle
from app.domain.indicators import simple_moving_average


def test_simple_moving_average_uses_last_candles() -> None:
    candles = []

    for day, price in enumerate(["10", "11", "12", "13"], start=1):
        close = Decimal(price)
        candle = Candle(
            timestamp=datetime(2026, 9, day, tzinfo=UTC),
            open=close,
            high=close,
            low=close,
            close=close,
            volume=Decimal(100),
        )
        candles.append(candle)

    result = simple_moving_average(candles, period=3)

    assert result == Decimal(12)


@pytest.mark.parametrize("period", [0, -1])
def test_simple_moving_average_rejects_invalid_period(period: int) -> None:
    with pytest.raises(
        ValueError,
        match="O período deve ser maior que zero.",
    ):
        simple_moving_average([], period=period)


def test_simple_moving_average_rejects_insufficient_candles() -> None:
    with pytest.raises(
        ValueError,
        match="Quantidade insuficiente de candles.",
    ):
        simple_moving_average([], period=3)
