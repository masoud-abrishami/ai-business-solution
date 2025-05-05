import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from .data_ingestion import load_data
from .logger import logger

model = None

def train_model():
    global model
    data = load_data()
    X = data[["year", "gdp", "population"]]
    y = data["sales"]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    logger.info("Model trained successfully")
    return model

def predict_sales(country=None):
    if model is None:
        train_model()
    
    data = load_data()
    if country:
        data = data[data["country"] == country]
        if data.empty:
            raise ValueError(f"No data for country: {country}")
    
    X = data[["year", "gdp", "population"]]
    predictions = model.predict(X)
    return predictions.tolist()