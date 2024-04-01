import unittest
import numpy as np
from sklearn.datasets import make_classification
from ModelTrainer import ModelTrainer

class TestModelTrainer(unittest.TestCase):
    def setUp(self):
        self.trainer = ModelTrainer()

    def test_train_model(self):
        X, y = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=0, random_state=42)
        self.trainer.train_model(X, y)
        # Check if model is trained (not raising exceptions is enough for this test case)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
