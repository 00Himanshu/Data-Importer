import json

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
    return transformed_data