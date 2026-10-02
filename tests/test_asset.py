from app.domain.asset import Asset, AssetType


def test_asset_stores_fields() -> None:
    asset = Asset(symbol="PETR4", name="Petrobras", asset_type=AssetType.STOCK)

    assert asset.symbol == "PETR4"
    assert asset.name == "Petrobras"
    assert asset.asset_type == AssetType.STOCK
