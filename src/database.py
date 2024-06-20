from astrapy.rest import create_client, RestClient
from config import ASTRA_DB_ID, ASTRA_DB_REGION, ASTRA_DB_KEYSPACE, ASTRA_DB_APPLICATION_TOKEN
from logger import setup_logging

logger = setup_logging()

def get_astra_db_client():
    try:
        client = create_client(
            astra_database_id=ASTRA_DB_ID,
            astra_database_region=ASTRA_DB_REGION,
            astra_application_token=AstraCS:cqCjyFNOxHARrdRUZRrmjtPb:b4376415711cf43ae9872fecbcf083ade838550607281f64099adb3c2a204c65
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
