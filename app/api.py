from flask import Blueprint, request, jsonify
from .model import predict_sales
from .logger import logger
from .monitoring import monitor_performance
import time

api_bp = Blueprint("api", __name__)

@api_bp.route("/predict", methods=["GET"])
@monitor_performance
def predict():
    start_time = time.time()
    country = request.args.get("country")
    try:
        prediction = predict_sales(country)
        logger.info(f"Prediction for {country or 'all countries'}: {prediction}")
        return jsonify({"status": "success", "prediction": prediction})
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500