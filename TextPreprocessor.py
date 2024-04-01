import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    def clean_text(self, text):
        # Remove non-alphanumeric characters
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

    def tokenize_text(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, tokens):
        return [word for word in tokens if word not in self.stop_words]

    def stem_words(self, tokens):
        return [self.stemmer.stem(word) for word in tokens]

    def preprocess_text(self, text):
        cleaned_text = self.clean_text(text)
        tokens = self.tokenize_text(cleaned_text)
        tokens = self.remove_stopwords(tokens)
        stemmed_tokens = self.stem_words(tokens)
        return stemmed_tokens

# Example
if __name__ == "__main__":
    preprocessor = TextPreprocessor()
    example_text = "Here's some sample text: With numbers (123) and symbols $#@!"
    processed_text = preprocessor.preprocess_text(example_text)
    print("Processed Text:", processed_text)
