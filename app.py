from flask import Flask, request, jsonify, render_template
import joblib
from src.logger import setup_logging
from src.database import get_collection

logger = setup_logging()
app = Flask(__name__)

MODEL_PATH = 'models\spam_classifier.pkl'
VECTORIZER_PATH = 'models\spam_classifier.pkl'
# VECTORIZER_PATH = 'models/vectorizer.pkl'

# Load the model and vectorizer
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    logger.info('Model and vectorizer loaded successfully')
except Exception as e:
    logger.error(f'Error loading model or vectorizer: {e}')
    raise

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.form['text']
        text_tfidf = vectorizer.transform([text])
        prediction = model.predict(text_tfidf)
        result = 'Spam' if prediction[0] else 'Not Spam'
        logger.info(f'Prediction made for input text: {text}')

        # Insert prediction into the database
        collection = get_collection('spam_data')
        collection.create_document({
            'text': text,
            'prediction': result
        })
        logger.info('Prediction inserted into the database')

        return render_template('index.html', prediction=result)
    except Exception as e:
        logger.error(f'Error making prediction: {e}')
        return render_template('index.html', prediction=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
