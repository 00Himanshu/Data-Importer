import unittest
from unittest.mock import patch
from data_importer.api_client import fetch_phone_data

class TestApiClient(unittest.TestCase):

    @patch('data_importer.api_client.requests.get')
    def test_fetch_phone_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": "1", "name": "Phone1", "data": {"color": "Black"}}]
        
        data = fetch_phone_data("https://api.restful-api.dev/objects")
        self.assertIsNotNone(data)
        self.assertEqual(data[0]['id'], "1")

if __name__ == '__main__':
    unittest.main()