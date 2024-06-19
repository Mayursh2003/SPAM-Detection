import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_data(data):
    # Basic preprocessing
    data = data.dropna()
    data['text'] = data['text'].str.lower()

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        data['text'], data['label'], test_size=0.2, random_state=42
    )

    # Convert text data to TF-IDF features
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    return X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer
