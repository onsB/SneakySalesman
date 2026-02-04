from pydantic import BaseModel, Field
from typing import List, Dict, Any, Literal, TypedDict


class AnalysisRequest(BaseModel):
    product: str
    location: str = "global"
    depth: str = "standard"


class ProductInfo(TypedDict):
    product: str
    price: float
    rating: float
    tier: Literal["budget", "midrange", "premium"]
    category: str
    seasonal: bool

class ProductReview(BaseModel):
    review_text: str
    rating: float = Field(ge=1.0, le=5.0, description="Rating between 1.0 and 5.0")  

class SentimentResult(BaseModel):
    overall_sentiment: str


class TrendResult(BaseModel):
    price_trend: str
    demand_trend: str


class PriceHistoryPoint(TypedDict):
    product: str
    date: str
    price: float


class PriceHistory(BaseModel):
    history: List[PriceHistoryPoint]


class DemandTrendPoint(TypedDict):
    product: str
    date: str
    number_of_orders: int


class DemandHistory(BaseModel):
    history: List[DemandTrendPoint]

class AnalysisResponse(BaseModel):
    data: str