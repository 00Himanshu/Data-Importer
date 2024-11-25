import requests
import logging
from data_importer.logger import setup_logger

setup_logger()
logger = logging.getLogger(__name__)

def fetch_phone_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching data from API: {e}")
        return None