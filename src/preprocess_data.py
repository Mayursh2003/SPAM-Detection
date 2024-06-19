import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from logger import setup_logging

logger = setup_logging()

def preprocess_data(data):
    try:
        # Basic preprocessing
        data = data.dropna()
        data['text'] = data['text'].str.lower()
        logger.info('Data preprocessing completed')

        # Split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            data['text'], data['label'], test_size=0.2, random_state=42
        )
        logger.info('Data split into training and testing sets')

        # Convert text data to TF-IDF features
        vectorizer = TfidfVectorizer(stop_words='english')
        X_train_tfidf = vectorizer.fit_transform(X_train)
        X_test_tfidf = vectorizer.transform(X_test)
        logger.info('Text data converted to TF-IDF features')

        return X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer
    except Exception as e:
        logger.error(f'Error during preprocessing: {e}')
        raise
