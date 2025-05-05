import pytest
from app.model import train_model, predict_sales
from unittest.mock import patch
import pandas as pd

@pytest.fixture
def mock_data():
    return pd.DataFrame({
        "country": ["USA", "China"],
        "year": [2020, 2020],
        "sales": [1000, 2000],
        "gdp": [1000000, 2000000],
        "population": [300000000, 1400000000]
    })

def test_train_model(mock_data):
    with patch("app.model.load_data", return_value=mock_data):
        model = train_model()
        assert model is not None
        assert hasattr(model, "predict")

def test_predict_sales_specific_country(mock_data):
    with patch("app.model.load_data", return_value=mock_data):
        with patch("app.model.train_model"):
            predictions = predict_sales("USA")
            assert len(predictions) == 1

def test_predict_sales_all_countries(mock_data):
    with patch("app.model.load_data", return_value=mock_data):
        with patch("app.model.train_model"):
            predictions = predict_sales()
            assert len(predictions) == 2