from datetime import UTC, datetime
from decimal import Decimal

from app.domain.asset import Asset, AssetType
from app.domain.candle import Candle
from app.domain.strategies import analyze_moving_average


def main() -> None:
    asset = Asset(symbol="DEMO", name="Ativo fictício", asset_type=AssetType.STOCK)
    candles = []

    for day, price in enumerate(["10", "11", "12", "13"], start=1):
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

    signal = analyze_moving_average(
        asset=asset,
        candles=candles,
        period=3,
        generated_at=datetime.now(tz=UTC),
    )

    print("Buy or Sell - análise com dados fictícios")
    print(f"Ativo: {signal.asset.symbol}")
    print(f"Sinal da estratégia: {signal.signal_type.name}")
    print(f"Motivo: {signal.reason}")
    print(f"Período: {signal.period} candles")
    print(f"Estratégia: {signal.strategy_name} v{signal.strategy_version}")
    print(f"Gerado em: {signal.generated_at.isoformat()}")


if __name__ == "__main__":
    main()
