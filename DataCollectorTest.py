import unittest
from unittest.mock import patch
from DataCollector import DataCollector

class TestDataCollector(unittest.TestCase):
    def setUp(self):
        self.api_key = "coo98khr01qm6hd1e1g0coo98khr01qm6hd1e1gg"
        self.collector = DataCollector(self.api_key)

    @patch('requests.get')
    def test_get_company_news_success(self, mock_get):
        # Mocking a successful API response
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [{"title": "Good news", "content": "Company is doing well"}]

        data = self.collector.get_company_news("AAPL", "2022-01-01", "2022-01-02")
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "Good news")

    @patch('requests.get')
    def test_get_company_news_failure(self, mock_get):
        # Mocking a failure API response
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        data = self.collector.get_company_news("AAPL", "2022-08-05", "2023-01-02")
        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()
