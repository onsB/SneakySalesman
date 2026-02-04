## SneakySalesman

Market analysis agent built with FastAPI and LangGraph. It exposes a simple API to run analysis workflows.

### Features
- FastAPI service for analysis requests
- Modular agent and utilities under `src/`
- Container-friendly setup with `uv`

### Requirements
- Python 3.12+
- Cohere API Key
- Optional: Docker

### Cohere API
Generate a Cohere API key (very accessible through free trial here: https://docs.aicontentlabs.com/articles/cohere-api-key/)

### Local setup
1. Install uv: `pip install uv`
2. Create a virtual environment and install dependencies: `uv sync`
3. Create a .env file under ./ and add the Cohere API key in it as follows:
- `COHERE_API_KEY="SAMPLEKEYVALUE"`
3. Run the app with FastAPI or Uvicorn.


### Run with Docker
Build the docker image:
- `docker build -t sneakysalesman:latest .`

Run (container on 80, host on 8000):
- `docker run -e COHERE_API_KEY="SAMPLEKEYVALUE" -p 8000:80 sneakysalesman:latest`

Then open http://localhost:8000 in your browser.

### Project structure
- `src/main.py`: FastAPI entrypoint
- `src/agent.py`: agent assembly
- `src/utils/`: helper utilities
- `test/`: test suite

### API
- Health check and endpoints are defined in `src/main.py`.

### Notes
- Ensure required environment variables are set if your agent depends on external APIs.
