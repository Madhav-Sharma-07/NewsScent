import unittest
from TextPreprocessor import TextPreprocessor

class TestTextPreprocessor(unittest.TestCase):
    def setUp(self):
        self.preprocessor = TextPreprocessor()

    def test_preprocess_text_empty(self):
        text = ""
        result = self.preprocessor.preprocess_text(text)
        self.assertEqual(result, [])

    def test_preprocess_text_normal(self):
        text = "Hello, World! This is a test."
        expected_result = ['hello', 'world', 'test']
        result = self.preprocessor.preprocess_text(text)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
