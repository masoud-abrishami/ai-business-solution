import logging
import os

logger = logging.getLogger("ai_business_solution")
logger.setLevel(logging.INFO)

# File handler
if not os.path.exists("logs"):
    os.makedirs("logs")
file_handler = logging.FileHandler("logs/app.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(console_handler)