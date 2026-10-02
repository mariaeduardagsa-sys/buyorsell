from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum

from app.domain.asset import Asset


class SignalType(Enum):
    BUY = "buy"
    HOLD = "hold"
    SELL = "sell"


@dataclass
class Signal:
    asset: Asset
    signal_type: SignalType
    reason: str
    generated_at: datetime
    strategy_name: str
    strategy_version: str
    period: int
    last_close: Decimal
    average: Decimal
    candle_timestamps: tuple[datetime, ...]
