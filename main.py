import pandas as pd
import numpy as np
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split

from DataCollector import DataCollector
from TextPreprocessor import TextPreprocessor
from FeatureExtractor import FeatureExtractor
from ModelTrainer import ModelTrainer
from ResultVisualizer import ResultVisualizer

# Setup NLTK VADER for sentiment analysis
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Initialize the DataCollector with your API key
api_key = "coo98khr01qm6hd1e1g0coo98khr01qm6hd1e1gg"
data_collector = DataCollector(api_key)

# List of companies to analyze
companies = ["AAPL"]

# Initialize visualizer
visualizer = ResultVisualizer()

for company_symbol in companies:
    # Fetch news articles for each company
    from_date = "2021-09-20"
    to_date = "2023-08-20"
    news_articles = data_collector.get_company_news(company_symbol, from_date, to_date)

    # Process and label data
    labels = []
    processed_texts = []
    preprocessor = TextPreprocessor()
    for article in news_articles:
        text = article['headline']
        processed_text = preprocessor.preprocess_text(text)
        score = sia.polarity_scores(' '.join(processed_text))  
        
        if score['compound'] >= 0.05:
            sentiment = 1  # Positive
        elif score['compound'] <= -0.05:
            sentiment = 0  # Negative
        else:
            sentiment = 2  # Neutral

        labels.append(sentiment)
        processed_texts.append(' '.join(processed_text))

    # Feature extraction
    extractor = FeatureExtractor(max_features=500)
    features = extractor.fit_transform(processed_texts)
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.25, random_state=42)

    # Train and evaluate model
    trainer = ModelTrainer(n_components=200)
    trainer.train_model(X_train, y_train)
    report = trainer.evaluate_model(X_test, y_test)
    print(f"Classification Report for {company_symbol}:\n", report)

    # Visualization of sentiment distribution
    visualizer.plot_sentiment_distribution(y_test, title=f"Sentiment Distribution for {company_symbol}")
