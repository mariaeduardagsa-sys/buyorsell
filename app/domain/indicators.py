from decimal import Decimal

from app.domain.candle import Candle


def simple_moving_average(candles: list[Candle], period: int) -> Decimal:
    if period <= 0:
        raise ValueError("O período deve ser maior que zero.")

    if len(candles) < period:
        raise ValueError("Quantidade insuficiente de candles.")

    recent_candles = candles[-period:]
    total = sum((candle.close for candle in recent_candles), start=Decimal(0))

    return total / Decimal(period)
