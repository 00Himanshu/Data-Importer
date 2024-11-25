import json
import logging
from data_importer.logger import setup_logger

setup_logger()
logger = logging.getLogger(__name__)

def transform_phone_data(api_response):
    transformed_data = []
    for item in api_response:
        phone_id = item.get('id')
        phone_name = item.get('name')
        phone_data = item.get('data', {})

        
        if phone_data is None:
            phone_data = {}
        
        transformed_data.append({
            'id': phone_id,
            'name': phone_name,
            'data': json.dumps(phone_data) 
        })
    logger.info("Transformed phone data into the required format")
    return transformed_data