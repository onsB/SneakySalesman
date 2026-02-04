from typing import List
from src.schemas import TrendResult, DemandHistory, DemandTrendPoint, PriceHistory, PriceHistoryPoint

from src.llm import llm_generate

# Mock data for price history and demand trends for different products
price_histories: List[PriceHistory] = [
    PriceHistory(
        history=[
            PriceHistoryPoint(product="Macbook Pro 2024", date="2024-01-01", price=2499.99),
            PriceHistoryPoint(product="Macbook Pro 2024", date="2024-02-01", price=2399.99),
            PriceHistoryPoint(product="Macbook Pro 2024", date="2024-03-01", price=2299.99),
            PriceHistoryPoint(product="Macbook Pro 2024", date="2024-04-01", price=2199.99),
            PriceHistoryPoint(product="Macbook Pro 2024", date="2024-05-01", price=2099.99),
        ]
    ),
    PriceHistory(
        history=[
            PriceHistoryPoint(product="Dell XPS 13", date="2024-01-01", price=1199.99),
            PriceHistoryPoint(product="Dell XPS 13", date="2024-02-01", price=1149.99),
            PriceHistoryPoint(product="Dell XPS 13", date="2024-03-01", price=1099.99),
            PriceHistoryPoint(product="Dell XPS 13", date="2024-04-01", price=1049.99),
            PriceHistoryPoint(product="Dell XPS 13", date="2024-05-01", price=999.99),
        ]
    ),
    PriceHistory(
        history=[
            PriceHistoryPoint(product="Acer Aspire 5", date="2024-01-01", price=549.99),
            PriceHistoryPoint(product="Acer Aspire 5", date="2024-02-01", price=529.99),
            PriceHistoryPoint(product="Acer Aspire 5", date="2024-03-01", price=499.99),
            PriceHistoryPoint(product="Acer Aspire 5", date="2024-04-01", price=479.99),
            PriceHistoryPoint(product="Acer Aspire 5", date="2024-05-01", price=459.99),
        ]
    ),
    PriceHistory(
        history=[
            PriceHistoryPoint(product="HP Spectre x360", date="2024-01-01", price=1399.99),
            PriceHistoryPoint(product="HP Spectre x360", date="2024-02-01", price=1349.99),
            PriceHistoryPoint(product="HP Spectre x360", date="2024-03-01", price=1299.99),
            PriceHistoryPoint(product="HP Spectre x360", date="2024-04-01", price=1249.99),
            PriceHistoryPoint(product="HP Spectre x360", date="2024-05-01", price=1199.99),
        ]
    ),
]

# Mpck data for demand trends for different products
demand_histories: List[DemandHistory] = [
    DemandHistory(
        history=[
            DemandTrendPoint(product="Macbook Pro 2024", date="2024-01-01", number_of_orders=150),
            DemandTrendPoint(product="Macbook Pro 2024", date="2024-02-01", number_of_orders=180),
            DemandTrendPoint(product="Macbook Pro 2024", date="2024-03-01", number_of_orders=200),
            DemandTrendPoint(product="Macbook Pro 2024", date="2024-04-01", number_of_orders=220),
            DemandTrendPoint(product="Macbook Pro 2024", date="2024-05-01", number_of_orders=250),
        ]
    ),
    DemandHistory(
        history=[
            DemandTrendPoint(product="Dell XPS 13", date="2024-01-01", number_of_orders=120),
            DemandTrendPoint(product="Dell XPS 13", date="2024-02-01", number_of_orders=130),
            DemandTrendPoint(product="Dell XPS 13", date="2024-03-01", number_of_orders=140),
            DemandTrendPoint(product="Dell XPS 13", date="2024-04-01", number_of_orders=150),
            DemandTrendPoint(product="Dell XPS 13", date="2024-05-01", number_of_orders=160),
        ]
    ),
    DemandHistory(
        history=[
            DemandTrendPoint(product="Acer Aspire 5", date="2024-01-01", number_of_orders=200),
            DemandTrendPoint(product="Acer Aspire 5", date="2024-02-01", number_of_orders=220),
            DemandTrendPoint(product="Acer Aspire 5", date="2024-03-01", number_of_orders=240),
            DemandTrendPoint(product="Acer Aspire 5", date="2024-04-01", number_of_orders=260),
            DemandTrendPoint(product="Acer Aspire 5", date="2024-05-01", number_of_orders=280),
        ]
    ),
    DemandHistory(
        history=[
            DemandTrendPoint(product="HP Spectre x360", date="2024-01-01", number_of_orders=130),
            DemandTrendPoint(product="HP Spectre x360", date="2024-02-01", number_of_orders=140),
            DemandTrendPoint(product="HP Spectre x360", date="2024-03-01", number_of_orders=150),
            DemandTrendPoint(product="HP Spectre x360", date="2024-04-01", number_of_orders=160),
            DemandTrendPoint(product="HP Spectre x360", date="2024-05-01", number_of_orders=170)]
)
]

def analyze_market_trends(product: str) -> TrendResult:
    price_prompt = f"""
    You are a market trends analyst. Based on the price history {price_histories} for 
    the product "{product}", provide a verdict on the current price trend for this product.
    Trend options: increasing, decreasing, stable.
    """
    price_trend = llm_generate(price_prompt)

    demand_prompt = f"""
    You are a market trends analyst. Based on the demand history {demand_histories} for 
    the product "{product}", provide a verdict on the current demand trend for this product.
    Trend options: increasing, decreasing, stable.
    """
    demand_trend = llm_generate(demand_prompt)

    return TrendResult(
        price_trend=price_trend,
        demand_trend=demand_trend,
    )
    