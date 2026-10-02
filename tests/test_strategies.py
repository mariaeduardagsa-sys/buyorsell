from datetime import UTC, datetime
from decimal import Decimal

import pytest

from app.domain.asset import Asset, AssetType
from app.domain.candle import Candle
from app.domain.signal import SignalType
from app.domain.strategies import (
    analyze_moving_average,
    moving_average_signal,
)


@pytest.mark.parametrize(
    "prices, expected",
    [
        (["10", "11", "12", "13"], SignalType.BUY),
        (["13", "12", "11", "10"], SignalType.SELL),
        (["10", "10", "10", "10"], SignalType.HOLD),
    ],
)
def test_moving_average_signal(prices: list[str], expected: SignalType) -> None:
    candles = []

    for day, price in enumerate(prices, start=1):
        close = Decimal(price)
        candles.append(
            Candle(
                timestamp=datetime(2026, 9, day, tzinfo=UTC),
                open=close,
                high=close,
                low=close,
                close=close,
                volume=Decimal(100),
            )
        )

    result = moving_average_signal(candles, period=3)
    assert result == expected


@pytest.mark.parametrize(
    ("prices", "expected_type", "expected_close", "expected_reason"),
    [
        (
            ["10", "11", "12", "13"],
            SignalType.BUY,
            Decimal(13),
            "O preço de fechamento (13) está acima da média móvel (12).",
        ),
        (
            ["14", "13", "12", "11"],
            SignalType.SELL,
            Decimal(11),
            "O preço de fechamento (11) está abaixo da média móvel (12).",
        ),
        (
            ["9", "12", "12", "12"],
            SignalType.HOLD,
            Decimal(12),
            "O preço de fechamento (12) está igual à média móvel (12).",
        ),
    ],
)
def test_analyze_moving_average_records_context(
    prices: list[str],
    expected_type: SignalType,
    expected_close: Decimal,
    expected_reason: str,
) -> None:
    asset = Asset(symbol="TEST", name="Ativo de exemplo", asset_type=AssetType.STOCK)
    generated_at = datetime(2026, 9, 5, tzinfo=UTC)
    candles = []

    for day, price in enumerate(prices, start=1):
        close = Decimal(price)
        candles.append(
            Candle(
                timestamp=datetime(2026, 9, day, tzinfo=UTC),
                open=close,
                high=close,
                low=close,
                close=close,
                volume=Decimal(100),
            )
        )

    result = analyze_moving_average(
        asset=asset,
        candles=candles,
        period=3,
        generated_at=generated_at,
    )

    assert result.asset == asset
    assert result.signal_type == expected_type
    assert result.reason == expected_reason
    assert result.generated_at == generated_at
    assert result.strategy_name == "simple_moving_average"
    assert result.strategy_version == "1.0.0"
    assert result.period == 3
    assert result.last_close == expected_close
    assert result.average == Decimal(12)
    assert result.candle_timestamps == (
        datetime(2026, 9, 2, tzinfo=UTC),
        datetime(2026, 9, 3, tzinfo=UTC),
        datetime(2026, 9, 4, tzinfo=UTC),
    )
