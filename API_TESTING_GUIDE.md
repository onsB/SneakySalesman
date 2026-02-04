# SneakySalesman - API Testing Guide

This guide matches the current tests in `test/test_main.py`.

## API Endpoints

### POST /analyze
Runs the market analysis pipeline from a single natural-language prompt.

**Request**
```json
{
  "request": "Analyze the market for MacBook Pro 2024."
}
```

**Response**
```json
{
  "data": "...report string..."
}
```

### GET /health
Health check endpoint.

**Response**
```json
{
  "status": "healthy"
}
```

## Tests

### Run all tests
```bash
pytest test/test_main.py -v
```

### Test classes
```bash
pytest test/test_main.py::TestHealthEndpoint -v
pytest test/test_main.py::TestAnalyzeEndpoint -v
```

### What is covered
- `/health` returns `{"status":"healthy"}`
- `/analyze` accepts `{"request": "..."}`
- `/analyze` returns a JSON object with `data` as a string
- Test prompts include MacBook Pro 2024, electric scooters, wireless earbuds, and smartwatches

## Local testing examples

### curl
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"request":"Analyze the market for electric scooters in Canada."}'

curl "http://localhost:8000/health"
```

### Python requests
```python
import requests

response = requests.post(
    "http://localhost:8000/analyze",
    json={"request": "Provide a market analysis for wireless earbuds in UK."},
)
print(response.json())
```

## Running the app

### Development
```bash
uvicorn src.main:app --reload
```

### Production
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

### Docker
```bash
docker build -t sneakysalesman:latest .
docker run -e COHERE_API_KEY="SAMPLEKEYVALUE" -p 8000:80 sneakysalesman:latest
```# SneakySalesman - API Testing Guide

## API Endpoints

### POST /analyze
Runs the market analysis pipeline from a single natural-language prompt.

**Request**
```json
{
  "request": "analyze the market for macbook pro 2024 in Montreal"
}
```

**Response**
```json
{
  "data": "...report string..."
}
```

### GET /health
Health check endpoint.

**Response**
```json
{
  "status": "healthy"
}
```

## Tests

### Run all tests
```bash
pytest test/test_main.py -v
```

### Run specific test classes
```bash
pytest test/test_main.py::TestHealthEndpoint -v
pytest test/test_main.py::TestAnalyzeEndpoint -v
```

### What is covered
- `/health` returns status `healthy`
- `/analyze` accepts a `request` string
- `/analyze` returns a JSON object with `data` as a string

## Local testing examples

### curl
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"request":"analyze the market for macbook pro 2024 in Montreal"}'

curl "http://localhost:8000/health"
```

### Python requests
```python
import requests

response = requests.post(
    "http://localhost:8000/analyze",
    json={"request": "analyze the market for macbook pro 2024 in Montreal"},
)
print(response.json())
```

## Running the app

### Development
```bash
uvicorn src.main:app --reload
```

### Production
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

### Docker
```bash
docker build -t sneakysalesman:latest .
docker run -e COHERE_API_KEY="SAMPLEKEYVALUE" -p 8000:80 sneakysalesman:latest
```# Sneaky Salesman - API Usage & Testing Guide

## New Features Added

### 1. **Location Parameter**
- Added `location` parameter to accept market/region information
- Defaults to `"global"` if not specified
- Examples: "USA", "France", "Japan", "Europe"

### 2. **Improved Response Structure**
- Returns structured response with status, product, location, and report
- Report includes: summary, insights, and recommendations

## API Endpoints

### POST `/analyze`
Perform market analysis for a product in a specific location.

**Request Format:**
```json
{
  "product": "laptop",
  "location": "USA",
  "depth": "standard"
}
```

**Parameters:**
- `product` (required): Name of the product to analyze
- `location` (optional): Market location. Default: "global"
- `depth` (optional): Analysis depth level. Options: "standard", "detailed". Default: "standard"

**Response Format:**
```json
{
  "status": "success",
  "product": "laptop",
  "location": "USA",
  "report": {
    "summary": "Market analysis summary...",
    "insights": {
      "key_insight_1": "...",
      "key_insight_2": "..."
    },
    "recommendations": [
      "Recommendation 1",
      "Recommendation 2"
    ]
  }
}
```

### GET `/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Testing

### Running All Tests
```bash
pytest test/test_main.py -v
```

### Running Specific Test Classes
```bash
# Test health endpoint
pytest test/test_main.py::TestHealthEndpoint -v

# Test analysis endpoint
pytest test/test_main.py::TestAnalyzeEndpoint -v

# Test input validation
pytest test/test_main.py::TestInputValidation -v
```

### Running Specific Tests
```bash
# Test with location parameter
pytest test/test_main.py::TestAnalyzeEndpoint::test_analyze_with_product_and_location -v

# Test response structure
pytest test/test_main.py::TestAnalyzeEndpoint::test_analyze_response_structure -v
```

## Local Testing Examples

### Using curl:
```bash
# Basic analysis (location defaults to global)
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"product": "laptop"}'

# Analysis with specific location
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"product": "smartphone", "location": "USA"}'

# Analysis with depth parameter
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"product": "watch", "location": "Japan", "depth": "detailed"}'

# Health check
curl "http://localhost:8000/health"
```

### Using Python requests:
```python
import requests

# Analyze product in specific market
response = requests.post(
    "http://localhost:8000/analyze",
    json={
        "product": "laptop",
        "location": "France"
    }
)
print(response.json())

# Analyze with depth
response = requests.post(
    "http://localhost:8000/analyze",
    json={
        "product": "smartphone",
        "location": "USA",
        "depth": "detailed"
    }
)
print(response.json())
```

## Starting the Application

### Development Mode
```bash
uvicorn src.main:app --reload
```

### Production Mode
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

### Using Docker
```bash
docker build -t sneaky-salesman .
docker run -p 8000:8000 sneaky-salesman
```

## Test Coverage

The test suite (`test/test_main.py`) includes:

1. **Health Check Tests**
   - Verifies health endpoint returns correct status

2. **Analysis Endpoint Tests**
   - Product-only analysis (location defaults to global)
   - Product + location analysis
   - Depth parameter handling
   - Multiple product/location combinations
   - Response structure validation

3. **Input Validation Tests**
   - Missing required fields
   - Empty strings
   - Special characters

## Key Improvements Made

✅ Added `location` parameter to the analysis request
✅ Updated `AgentState` to include location
✅ Modified agent pipeline to use location information
✅ Added `AnalysisResponse` schema for structured responses
✅ Created comprehensive test suite with 10+ test cases
✅ Health check endpoint for monitoring

## Files Modified

- `src/schemas.py` - Added location field and response model
- `src/agent.py` - Updated state and pipeline
- `src/main.py` - Updated endpoint to accept location
- `test/test_main.py` - New comprehensive test suite
