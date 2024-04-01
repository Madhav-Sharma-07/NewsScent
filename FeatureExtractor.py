from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix

class FeatureExtractor:
    def __init__(self, max_features=1000):
        self.vectorizer = TfidfVectorizer(max_features=max_features)

    def fit_transform(self, documents):
        if not documents:
            return csr_matrix((0, self.vectorizer.max_features))
        return self.vectorizer.fit_transform(documents)

    def transform(self, documents):
        return self.vectorizer.transform(documents)
