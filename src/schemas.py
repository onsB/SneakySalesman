from pydantic import BaseModel
from typing import Dict, List, Any

class MarketRequest(BaseModel):
    product: str
    market: str
    region: str

class MarketResponse(BaseModel):
    product: str
    insights: Dict[str, Any]
    recommendations: List[str]

