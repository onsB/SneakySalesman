from fastapi import FastAPI, HTTPException
from src.agent import MarketAgent
from src.schemas import MarketRequest, MarketResponse

app = FastAPI(title="Market Intelligence Agent")

agent = MarketAgent()

@app.post("/analyze", response_model=MarketResponse)
def analyze_market(request: MarketRequest):
    try:
        return agent.run(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
