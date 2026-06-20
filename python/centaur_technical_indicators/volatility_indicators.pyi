# Type stubs for centaur_technical_indicators.volatility_indicators
# Auto-generated from the Rust binding signatures; keep in sync with src/volatility_indicators.rs.

class single:
    @staticmethod
    def ulcer_index(prices: list[float]) -> float: ...

class bulk:
    @staticmethod
    def ulcer_index(prices: list[float], period: int) -> list[float]: ...
    @staticmethod
    def volatility_system(high: list[float], low: list[float], close: list[float], period: int, constant_multiplier: float, constant_model_type: str) -> list[float]: ...

