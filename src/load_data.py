import pandas as pd
from logger import setup_logging

logger = setup_logging()

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logger.info(f'Data loaded successfully from {file_path}')
        return data
    except Exception as e:
        logger.error(f'Error loading data from {file_path}: {e}')
        raise
