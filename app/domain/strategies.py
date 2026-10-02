from datetime import datetime

from app.domain.asset import Asset
from app.domain.candle import Candle
from app.domain.indicators import simple_moving_average
from app.domain.signal import Signal, SignalType


def moving_average_signal(
    candles: list[Candle],
    period: int,
) -> SignalType:
    average = simple_moving_average(candles, period)
    last_close = candles[-1].close

    if last_close > average:
        return SignalType.BUY

    if last_close < average:
        return SignalType.SELL

    return SignalType.HOLD


def analyze_moving_average(
    asset: Asset,
    candles: list[Candle],
    period: int,
    generated_at: datetime,
) -> Signal:
    signal_type = moving_average_signal(candles, period)
    average = simple_moving_average(candles, period)
    last_close = candles[-1].close

    if signal_type == SignalType.BUY:
        reason = f"O preço de fechamento ({last_close}) está acima da média móvel ({average})."
    elif signal_type == SignalType.SELL:
        reason = f"O preço de fechamento ({last_close}) está abaixo da média móvel ({average})."
    else:
        reason = f"O preço de fechamento ({last_close}) está igual à média móvel ({average})."

    return Signal(
        asset=asset,
        signal_type=signal_type,
        reason=reason,
        generated_at=generated_at,
        strategy_name="simple_moving_average",
        strategy_version="1.0.0",
        period=period,
        last_close=last_close,
        average=average,
        candle_timestamps=tuple(candle.timestamp for candle in candles[-period:]),
    )
