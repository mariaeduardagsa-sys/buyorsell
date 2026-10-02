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
