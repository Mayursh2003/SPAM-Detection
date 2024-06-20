# logger.py
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("astra_db_logger")
    return logger
