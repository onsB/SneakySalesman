from fastapi import FastAPI
from src.agent import build_agent
from src.schemas import AnalysisRequest, AnalysisResponse

app = FastAPI(title="Sneaky Salesman: market analysis agent")

agent = build_agent()


@app.post("/analyze", response_model=AnalysisResponse)
def analyze(request: AnalysisRequest):
    result = agent.invoke({
        "product": request.product,
        "location": request.location,
    })
    return {
        "status": "success",
        "product": request.product,
        "location": request.location,
        "report": result["report"],
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
