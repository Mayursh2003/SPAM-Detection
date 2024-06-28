# src/predict.py

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the model and vectorizer
model = joblib.load('models/spam_classifier.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

def predict(text):
    # Vectorize the input text
    X = vectorizer.transform([text])
    # Predict using the loaded model
    prediction = model.predict(X)
    return prediction[0]

if __name__ == "__main__":
    sample_text = "Congratulations! You've won a free ticket to the Bahamas!"
    prediction = predict(sample_text)
    print(f"The predicted label for the sample text is: {'Spam' if prediction == 1 else 'Ham'}")
