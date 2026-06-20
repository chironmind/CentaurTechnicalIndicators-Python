# Type stubs for centaur_technical_indicators.moving_average
# Auto-generated from the Rust binding signatures; keep in sync with src/moving_average.rs.

class single:
    @staticmethod
    def mcginley_dynamic(latest_price: float, previous_mcginley_dynamic: float, period: int) -> float: ...
    @staticmethod
    def moving_average(prices: list[float], moving_average_type: str) -> float: ...

class bulk:
    @staticmethod
    def mcginley_dynamic(prices: list[float], previous_mcginley_dynamic: float, period: int) -> list[float]: ...
    @staticmethod
    def moving_average(prices: list[float], moving_average_type: str, period: int) -> list[float]: ...

