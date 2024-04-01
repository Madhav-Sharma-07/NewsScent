import unittest
from ResultVisualizer import ResultVisualizer

class TestResultVisualizer(unittest.TestCase):
    def setUp(self):
        self.visualizer = ResultVisualizer()

    def test_plot_sentiment_distribution(self):
        try:
            self.visualizer.plot_sentiment_distribution([1, 0, 2], title="Test Plot")
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"plot_sentiment_distribution raised an exception {e}")

if __name__ == '__main__':
    unittest.main()
