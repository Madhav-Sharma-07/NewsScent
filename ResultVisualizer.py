import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class ResultVisualizer:
    def __init__(self):
        # Setting the aesthetic style of the plots
        sns.set(style="whitegrid", palette="pastel")

    def plot_sentiment_distribution(self, sentiments, title="Sentiment Distribution"):
        # Counting the occurrences of each sentiment
        sentiment_counts = {x: sentiments.count(x) for x in set(sentiments)}

        # Preparing the data for plotting
        labels = ['Negative', 'Positive', 'Neutral']
        values = [sentiment_counts.get(i, 0) for i in range(3)]  # Assuming 0=negative, 1=positive, 2=neutral

        # Creating the bar plot
        plt.figure(figsize=(8, 6))
        sns.barplot(x=labels, y=values, palette='viridis')
        plt.title(title)
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()    

    # Unimplemented due to data limitations
    def plot_sentiment_over_time(self, data, title="Sentiment Over Time"):
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='date', y='sentiment', data=data, marker='o', palette='coolwarm', linewidth=2.5)
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel('Sentiment Score')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Unimplemented due to data limitations
    def plot_sentiment_heatmap(self, data, title="Sentiment Heatmap"):
        plt.figure(figsize=(10, 8))
        sns.heatmap(data, annot=True, fmt=".1f", linewidths=.5, cmap='Blues')
        plt.title(title)
        plt.xlabel('Category')
        plt.ylabel('Date')
        plt.tight_layout()
        plt.show()

# Example
if __name__ == "__main__":
    visualizer = ResultVisualizer()
    example_sentiments = [1, 1, 2, 0, 0, 0, 1, 2, 2, 1]
    visualizer.plot_sentiment_distribution(example_sentiments)

    # Example data for sentiment over time (mock data)
    dates = pd.date_range(start='2021-01-01', periods=10, freq='M')
    sentiment_scores = np.random.randint(0, 3, size=10)
    time_data = pd.DataFrame({'date': dates, 'sentiment': sentiment_scores})
    visualizer.plot_sentiment_over_time(time_data)

    # Example data for heatmap
    heatmap_data = pd.DataFrame(np.random.randint(0, 3, size=(10, 3)), index=pd.date_range("2021-01-01", periods=10, freq='M'), columns=['Product A', 'Product B', 'Product C'])
    visualizer.plot_sentiment_heatmap(heatmap_data)
