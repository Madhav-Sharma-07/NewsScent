from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV
import joblib

class ModelTrainer:
    def __init__(self, n_components=None):
        self.svd = TruncatedSVD(n_components=n_components) if n_components is not None else None
        # Initialize multiple models
        self.models = [
            ('lr', LogisticRegression()),
            ('svm', SVC(probability=True)),
            ('rf', RandomForestClassifier())
        ]
        # Setup the voting classifier without specifying parameters yet
        self.classifier = VotingClassifier(estimators=self.models, voting='soft')

    def train_model(self, X, y):
       if self.svd:
         X = self.svd.fit_transform(X) 

       # Initialize models with the best parameters from GridSearch
       self.models = [
          ('lr', LogisticRegression(C=10, solver='saga', max_iter=1000)),  # Best parameters for Logistic Regression
          ('svm', SVC(C=100, kernel='rbf', gamma='auto', probability=True)),  # Best parameters for SVM
          ('rf', RandomForestClassifier(n_estimators=100, max_depth=30, min_samples_split=10))  # Best parameters for RandomForest
       ]

       # Setup the voting classifier with these models
       self.classifier = VotingClassifier(estimators=self.models, voting='soft')
       self.classifier.fit(X, y) 

       # Commented out GridSearchCV for future use if needed
       # param_grid = {
       #     'lr__C': [0.1, 1, 10],  # Extending the range of C for Logistic Regression
       #     'lr__solver': ['liblinear', 'saga'],  # Including different solvers
       #     'svm__C': [10, 100],  # Extended range of C for SVM
       #     'svm__kernel': ['linear', 'rbf', 'poly'],  # Testing multiple kernel types
       #     'svm__gamma': ['scale', 'auto'],  # Extended range of gamma values
       #     'rf__n_estimators': [100, 200, 300],  # More options for the number of trees
       #     'rf__max_depth': [None, 30],  # Deeper trees for Random Forest
       #     'rf__min_samples_split': [5, 10]  # Including min samples split for Random Forest
       # }
       # grid_search = GridSearchCV(self.classifier, param_grid, cv=5, scoring='accuracy', verbose=2)
       # grid_search.fit(X, y)
       # self.classifier = grid_search.best_estimator_  # Update the classifier with the best found parameters

    def evaluate_model(self, X, y):
        if self.svd:
            X = self.svd.transform(X)
        predictions = self.classifier.predict(X)
        print("Accuracy:", accuracy_score(y, predictions))
        return classification_report(y, predictions)

    def save_model(self, file_name):
        joblib.dump(self.classifier, f"{file_name}_voting_classifier.pkl")
        if self.svd:
            joblib.dump(self.svd, f"{file_name}_svd.pkl")

# Example of initializing and using the ModelTrainer with SVD and simplified hyperparameter tuning
trainer = ModelTrainer(n_components=50)
