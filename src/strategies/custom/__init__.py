"""
🌙 Moon Dev's Custom Strategies Package
"""
from src.strategies.base_strategy import BaseStrategy
from .example_strategy import ExampleStrategy
from .private_my_strategy import MyStrategy
from .private_rsi_volume_strategy import RSIVolumeStrategy
from .private_bollinger_strategy import BollingerMeanReversionStrategy
from .private_macd_momentum_strategy import MACDMomentumStrategy
from .private_confluence_strategy import MultiIndicatorConfluenceStrategy
from .private_ema_volume_strategy import EMAVolumeStrategy

__all__ = [
    'ExampleStrategy',
    'MyStrategy',
    'RSIVolumeStrategy',
    'BollingerMeanReversionStrategy',
    'MACDMomentumStrategy',
    'MultiIndicatorConfluenceStrategy',
    'EMAVolumeStrategy'
] 