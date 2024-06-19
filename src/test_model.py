import joblib

def load_model(model_path, vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer

def predict_spam(text, model, vectorizer):
    text_tfidf = vectorizer.transform([text])
    prediction = model.predict(text_tfidf)
    return prediction[0]

MODEL_PATH = 'models/spam_classifier.pkl'
VECTORIZER_PATH = 'models/vectorizer.pkl'

if __name__ == '__main__':
    model, vectorizer = load_model(MODEL_PATH, VECTORIZER_PATH)
    text = "Free money!!! Claim your prize now!"
    result = predict_spam(text, model, vectorizer)
    print(f"Predicted label: {'Spam' if result else 'Not Spam'}")
