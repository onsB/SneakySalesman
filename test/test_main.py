import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.schemas import InitialRequest


client = TestClient(app)


class TestHealthEndpoint:
    """Test health check endpoint"""
    
    def test_001_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}


class TestAnalyzeEndpoint:
    """Test main analysis endpoint"""
    
    def test_001_analyze_with_product_only(self):
        try:
            """Test analysis with only product name (location defaults to global)"""
            request = InitialRequest(request="I want to analyze the market for MacBook Pro 2024.")
            response = client.post("/analyze", json=request.model_dump())
            
            assert response.status_code == 200
            data = response.json()
            assert data["data"] is not None
            assert "2024" in data["data"]
        except Exception as e:
            pytest.fail(f"Test failed due to an exception: {e}")
    
    def test_002_analyze_with_product_and_location(self):
        try:
            """Test analysis with both product and location"""
            request = InitialRequest(request="Analyze the market for electric scooters in Canada.")
            response = client.post("/analyze", json=request.model_dump())
            
            assert response.status_code == 200
            data = response.json()
            assert data["data"] is not None
            assert "scooter" in data["data"]
        except Exception as e:
            pytest.fail(f"Test failed due to an exception: {e}")
    
    def test_003_analyze_with_parameter(self):
        try:
            """Test analysis with parameter"""
            request = InitialRequest(request="Provide a market analysis for wireless earbuds in UK.")
            response = client.post("/analyze", json=request.model_dump())
            
            assert response.status_code == 200
            data = response.json()
            assert data["data"] is not None
            assert "earbuds" in data["data"]
        except Exception as e:
            pytest.fail(f"Test failed due to an exception: {e}")
    
    def test_004_analyze_response_structure(self):
        try:
            """Test that the response structure is correct"""
            request = InitialRequest(request="Analyze the market for smartwatches in Germany.")
            response = client.post("/analyze", json=request.model_dump())
            
            assert response.status_code == 200
            data = response.json()
            assert "data" in data
            assert isinstance(data["data"], str)
        except Exception as e:
            pytest.fail(f"Test failed due to an exception: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
