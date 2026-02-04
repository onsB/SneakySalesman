from fastapi import FastAPI
from src.agent import build_agent
from src.schemas import InitialRequest, AnalysisResponse

app = FastAPI(title="Sneaky Salesman: market analysis agent")

agent = build_agent()


@app.post("/analyze", response_model=AnalysisResponse)
def analyze(request: InitialRequest):
    result = agent.invoke({
        "user_request": request.request
    })
    return AnalysisResponse(data=result["report"])

@app.get("/health")
def health():
    return {"status": "healthy"}
