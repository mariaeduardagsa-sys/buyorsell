from datetime import UTC, datetime, timedelta
from decimal import Decimal, InvalidOperation

from app.domain.asset import Asset, AssetType
from app.domain.candle import Candle
from app.domain.strategies import analyze_moving_average


def main() -> None:
    asset = Asset(symbol="DEMO", name="Ativo fictício", asset_type=AssetType.STOCK)
    prices_text = input(
        "Digite os fechamentos do mais antigo ao mais recente "
        "(separados por espaço; use ponto decimal): "
    )

    prices = prices_text.split()
    candles = []
    start_at = datetime(2026, 9, 1, tzinfo=UTC)

    for index, price in enumerate(prices):
        try:
            close = Decimal(price)
        except InvalidOperation:
            print(f"Preço inválido: {price}. Certifique-se de usar ponto decimal.")
            return

        if not close.is_finite() or close <= 0:
            print(
                f"Preço inválido: {price}. O preço deve ser um número positivo finito."
            )
            return

        candles.append(
            Candle(
                timestamp=start_at + timedelta(days=index),
                open=close,
                high=close,
                low=close,
                close=close,
                volume=Decimal(100),
            )
        )

    try:
        signal = analyze_moving_average(
            asset=asset,
            candles=candles,
            period=3,
            generated_at=datetime.now(tz=UTC),
        )
    except ValueError as error:
        print(f"Erro ao analisar os dados: {error}")
        return

    print("Buy or Sell - análise com dados fictícios")
    print(f"Ativo: {signal.asset.symbol}")
    print(f"Sinal da estratégia: {signal.signal_type.name}")
    print(f"Motivo: {signal.reason}")
    print(f"Período: {signal.period} candles")
    print(f"Estratégia: {signal.strategy_name} v{signal.strategy_version}")
    print(f"Gerado em: {signal.generated_at.isoformat()}")


if __name__ == "__main__":
    main()
