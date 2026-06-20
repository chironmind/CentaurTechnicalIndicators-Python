# Type stubs for centaur_technical_indicators.correlation_indicators
# Auto-generated from the Rust binding signatures; keep in sync with src/correlation_indicators.rs.

class single:
    @staticmethod
    def correlate_asset_prices(prices_asset_a: list[float], prices_asset_b: list[float], constant_model_type: str, deviation_model: str) -> float: ...

class bulk:
    @staticmethod
    def correlate_asset_prices(prices_asset_a: list[float], prices_asset_b: list[float], constant_model_type: str, deviation_model: str, period: int) -> list[float]: ...

