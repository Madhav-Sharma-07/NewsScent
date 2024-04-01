import unittest
from FeatureExtractor import FeatureExtractor
from sklearn.feature_extraction.text import TfidfVectorizer

class TestFeatureExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = FeatureExtractor(max_features=100)

    def test_fit_transform_empty(self):
        texts = []
        result = self.extractor.fit_transform(texts)
        self.assertEqual(result.shape[0], 0)

    def test_fit_transform_non_empty(self):
        texts = ["This is a test.", "Another test document."]
        result = self.extractor.fit_transform(texts)
        self.assertEqual(result.shape[0], 2)  
        vectorizer = TfidfVectorizer(max_features=100)
        expected_result = vectorizer.fit_transform(texts)
        
        self.assertEqual(result.shape[1], expected_result.shape[1], 
                         f"Expected {expected_result.shape[1]} features, got {result.shape[1]}")


if __name__ == '__main__':
    unittest.main()
