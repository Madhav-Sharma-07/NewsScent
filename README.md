# Sentiment Analysis of News Articles

## Project Overview
This project is designed to perform sentiment analysis on news articles related to specific companies or topics. It utilizes a combination of Python libraries and machine learning techniques to preprocess text data, train sentiment classification models, and visualize the results. This is my final project for CIS 1902: Python Programming at the University of Pennsylvania in Spring 2024.

## Features and Components

This section details the functionalities and structural components of the sentiment analysis project, outlining how each part contributes to the overall system.

### DataCollector
- **Functionality**: Fetches news articles via an API to provide data for sentiment analysis.
- **Key Feature**: Integrates with web APIs to automatically retrieve and format news data for further processing.

### TextPreprocessor
- **Functionality**: Cleans and preprocesses the text data, preparing it for analysis.
- **Key Feature**: Implements various text normalization techniques such as tokenization, removal of stopwords, and punctuation, which are crucial for reliable data analysis.

### FeatureExtractor
- **Functionality**: Transforms cleaned text data into a numerical format that machine learning models can process.
- **Key Feature**: Uses techniques like TF-IDF to convert text into feature vectors, highlighting the importance of different words for sentiment analysis.

### ModelTrainer
- **Functionality**: Trains machine learning models to classify the sentiment of the text data accurately.
- **Key Feature**: Employs a variety of models, including Logistic Regression, SVM, and Random Forest within a Voting Classifier framework to enhance prediction accuracy.

### ResultVisualizer
- **Functionality**: Visualizes the results of the sentiment analysis to make the insights accessible and understandable.
- **Key Feature**: Generates various plots such as bar charts for sentiment distribution and line plots for sentiment trends over time, using libraries like Matplotlib and Seaborn for high-quality visual output.

## System Requirements

- Python 3.8 or higher
- Pip package manager

## Libraries Used

This project relies on several key Python libraries to handle various tasks such as data collection, processing, machine learning, and visualization. Below is a detailed list of these libraries and their roles in the project:

- **NumPy**: Utilized for high-performance numerical operations and array manipulation, essential for handling large datasets and features.
- **Pandas**: Provides data structures and data analysis tools, making it easier to manipulate and prepare data for modeling.
- **Scikit-learn**: Used for machine learning, offering versatile tools for data mining and analysis. It's employed here primarily for building and tuning models, as well as for performing various transformations and predictions.
- **Matplotlib & Seaborn**: These libraries are used for plotting graphs and visualizations to represent the data and results of the sentiment analysis visually.
- **NLTK (Natural Language Toolkit)**: A leading platform for building Python programs to work with human language data. It is used extensively for processing the text data, including tasks such as tokenization and sentiment analysis using its VADER tool.
- **Joblib**: Used for saving and loading machine learning models, which is particularly useful for deploying models or moving them between different phases of development.
- **Seaborn**: An advanced visualization library based on matplotlib; it provides a high-level interface for drawing attractive and informative statistical graphics.
- **Requests**: This library is used for making HTTP requests to web APIs, essential for the `DataCollector` component to fetch news data.

## Future Work

While the current implementation of the sentiment analysis project has achieved a foundational level of functionality and insight, there are several areas for further development and enhancement to increase accuracy and utility:

1. **Enhance Data Collection**: The free version of the API used to fetch news articles imposes limits on the amount of text retrievable, which restricts the volume of data available for training the models. Expanding data sources, possibly by integrating premium API services or additional free sources, would provide more comprehensive data sets for training and could significantly improve model accuracy.

2. **Real-Time Analysis Capability**: Developing the ability to perform sentiment analysis in real-time would greatly enhance the application's utility for businesses and analysts. 

3. **Sentiment Granularity**: Beyond classifying sentiments simply as positive, negative, or neutral, exploring more granular sentiments or emotions (such as happy, sad, angry, etc.)

4. **Better Implement ResultVisualizer**: I implemeneted methods in this class to generate a heatmap and a sentiment over time graph, but currently the free API had some issues with giving me the specific dates associated with each piece of text (instead it just gives me all the text in that date range.) So, once I have the premium API I can simply implement these methods in the main.py and improve the visualization.
