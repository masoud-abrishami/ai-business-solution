import pytest
from app import create_app
from unittest.mock import patch

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_predict_specific_country(client):
    with patch("app.api.predict_sales", return_value=[1000.0]):
        response = client.get("/predict?country=USA")
        assert response.status_code == 200
        assert response.json["status"] == "success"
        assert response.json["prediction"] == [1000.0]

def test_predict_all_countries(client):
    with patch("app.api.predict_sales", return_value=[1000.0, 2000.0]):
        response = client.get("/predict")
        assert response.status_code == 200
        assert response.json["status"] == "success"
        assert response.json["prediction"] == [1000.0, 2000.0]

def test_predict_invalid_country(client):
    with patch("app.api.predict_sales", side_effect=ValueError("No data for country: Invalid")):
        response = client.get("/predict?country=Invalid")
        assert response.status_code == 500
        assert response.json["status"] == "error"