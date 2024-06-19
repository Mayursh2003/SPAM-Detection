import joblib
from logger import setup_logging

logger = setup_logging()

def load_model(model_path, vectorizer_path):
    try:
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        logger.info('Model and vectorizer loaded successfully')
        return model, vectorizer
    except Exception as e:
        logger.error(f'Error loading model or vectorizer: {e}')
        raise

def predict_spam(text, model, vectorizer):
    try:
        text_tfidf = vectorizer.transform([text])
        prediction = model.predict(text_tfidf)
        logger.info(f'Prediction made for input text')
        return prediction[0]
    except Exception as e:
        logger.error(f'Error making prediction: {e}')
        raise

MODEL_PATH = 'models/spam_classifier.pkl'
VECTORIZER_PATH = 'models/vectorizer.pkl'

if __name__ == '__main__':
    try:
        model, vectorizer = load_model(MODEL_PATH, VECTORIZER_PATH)
        text = "Free money!!! Claim your prize now!"
        result = predict_spam(text, model, vectorizer)
        logger.info(f'Predicted label: {"Spam" if result else "Not Spam"}')
    except Exception as e:
        logger.error(f'Error in testing script: {e}')
