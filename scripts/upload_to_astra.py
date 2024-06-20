import pandas as pd
from astrapy.rest import create_client
import uuid
from config import ASTRA_DB_ID, ASTRA_DB_REGION, ASTRA_DB_KEYSPACE, ASTRA_DB_APPLICATION_TOKEN
from logger import setup_logging

logger = setup_logging()

def get_astra_db_client():
    try:
        client = create_client(
            astra_database_id=ASTRA_DB_ID,
            astra_database_region=ASTRA_DB_REGION,
            astra_application_token=ASTRA_DB_APPLICATION_TOKEN
        )
        logger.info('Connected to Astra DB successfully')
        return client
    except Exception as e:
        logger.error(f'Error connecting to Astra DB: {e}')
        raise

def get_collection(collection_name):
    try:
        client = get_astra_db_client()
        db = client.namespace(ASTRA_DB_KEYSPACE)
        collection = db.collection(collection_name)
        logger.info(f'Collection {collection_name} accessed successfully')
        return collection
    except Exception as e:
        logger.error(f'Error accessing collection {collection_name}: {e}')
        raise

# Load your CSV data
df = pd.read_csv('data/spam_data.csv')

# Convert DataFrame to a list of dictionaries
data = df.to_dict(orient='records')

# Insert data into Astra DB
collection = get_collection('spam_data')

for record in data:
    record['id'] = str(uuid.uuid4())  # Generate a unique ID for each record
    collection.create_document(record)

logger.info("Data uploaded to Astra DB successfully.")
