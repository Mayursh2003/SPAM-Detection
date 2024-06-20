from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
from .logger import setup_logging

logger = setup_logging()

def train_model(X_train, y_train):
    try:
        model = LogisticRegression()
        model.fit(X_train, y_train)
        logger.info('Model training completed')
        return model
    except Exception as e:
        logger.error(f'Error during model training: {e}')
        raise

def evaluate_model(model, X_test, y_test):
    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        logger.info(f'Model evaluation completed with accuracy: {accuracy * 100:.2f}%')
        return accuracy
    except Exception as e:
        logger.error(f'Error during model evaluation: {e}')
        raise

def save_model(model, vectorizer, model_path, vectorizer_path):
    try:
        joblib.dump(model, model_path)
        joblib.dump(vectorizer, vectorizer_path)
        logger.info(f'Model saved to {model_path} and vectorizer saved to {vectorizer_path}')
    except Exception as e:
        logger.error(f'Error saving model or vectorizer: {e}')
        raise
