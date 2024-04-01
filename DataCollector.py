import requests

class DataCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://finnhub.io/api/v1/"

    # Fetch news articles
    def get_company_news(self, company_symbol, from_date, to_date):
        endpoint = f"company-news?symbol={company_symbol}&from={from_date}&to={to_date}&token={self.api_key}"
        url = self.base_url + endpoint

        try:
            response = requests.get(url)
            if response.status_code == 200:
                news_data = response.json()
                return news_data
            else:
                print(f"Failed to fetch news for {company_symbol}. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    # Option to quickly fetch financial metrics if needed 
    def get_basic_financials(self, company_symbol, metric='all'):
        endpoint = f"stock/metric?symbol={company_symbol}&metric={metric}&token={self.api_key}"
        url = self.base_url + endpoint

        try:
            response = requests.get(url)
            if response.status_code == 200:
                financial_data = response.json()
                return financial_data
            else:
                print(f"Failed to fetch financials for {company_symbol}. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None



# Example
if __name__ == "__main__":
    api_key = "coo98khr01qm6hd1e1g0coo98khr01qm6hd1e1gg"  # Replace with your API key
    data_collector = DataCollector(api_key)
    company_symbol = "AAPL"
    from_date = "2023-08-15"
    to_date = "2023-08-20"

    # Fetch news articles
    news_articles = data_collector.get_company_news(company_symbol, from_date, to_date)
    if news_articles:
        print("News Articles:")
        for article in news_articles:
            print(article)
    else:
        print("Failed to fetch news.")

    # Fetch financial metrics
    financial_metrics = data_collector.get_basic_financials(company_symbol)
    if financial_metrics:
        print("\nFinancial Metrics:")
        print(financial_metrics)
    else:
        print("Failed to fetch financial metrics.")
