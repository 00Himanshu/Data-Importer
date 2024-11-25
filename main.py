import yaml
from data_importer.api_client import fetch_phone_data
from data_importer.db import insert_phone_data
from data_importer.models import transform_phone_data

def main():
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    api_url = config['api']['url']
    phone_data = fetch_phone_data(api_url)
    
    if phone_data:
        transformed_data= transform_phone_data(phone_data)
        insert_phone_data(transformed_data)

if __name__ == "__main__":
    main()