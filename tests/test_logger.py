import pytest
import logging
from app.logger import logger

def test_logger_info():
    with pytest.raises(Exception):  # Logger doesn't raise, just testing log creation
        logger.info("Test info message")
        assert True

def test_logger_error():
    with pytest.raises(Exception):
        logger.error("Test error message")
        assert True