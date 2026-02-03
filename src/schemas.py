from pydantic import BaseModel
from typing import List, Dict, Any


class AnalysisRequest(BaseModel):
    product: str
    location: str = "global"
    depth: str = "standard"


class ProductData(BaseModel):
    platform: str
    price: float
    rating: float
    reviews_count: int


class SentimentResult(BaseModel):
    overall_sentiment: str
    key_themes: List[str]


class TrendResult(BaseModel):
    price_trend: str
    demand_trend: str
    competitors: List[str]


class FinalReport(BaseModel):
    summary: str
    insights: Dict[str, Any]
    recommendations: List[str]

class AnalysisResponse(BaseModel):
    status: str
    product: str
    location: str
    report: FinalReport