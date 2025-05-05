import pandas as pd
from .logger import logger

def load_data():
    try:
        data = pd.read_csv("data/sample_sales_data.csv")
        logger.info("Data loaded successfully")
        return data
    except Exception as e:
        logger.error(f"Data ingestion error: {str(e)}")
        raise