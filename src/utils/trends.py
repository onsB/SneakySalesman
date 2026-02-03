from src.schemas import TrendResult


def analyze_market_trends(product: str) -> TrendResult:
    return TrendResult(
        price_trend="stable",
        demand_trend="increasing",
        competitors=["Samsung Galaxy S24", "Google Pixel 8"],
    )