from dataclasses import dataclass
from enum import Enum


class AssetType(Enum):
    STOCK = "stock"
    ETF = "etf"
    CRYPTO = "crypto"


@dataclass
class Asset:
    symbol: str
    name: str
    asset_type: AssetType

    def __post_init__(self) -> None:
        if not self.symbol.strip():
            raise ValueError("O símbolo do ativo não pode ser vazio.")
