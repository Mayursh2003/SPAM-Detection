from load_data import load_data
from preprocess_data import preprocess_data
from train_model import train_model, evaluate_model, save_model

DATA_PATH = 'path_to_your_data.csv'
MODEL_PATH = 'models/spam_classifier.pkl'
VECTORIZER_PATH = 'models/vectorizer.pkl'

def main():
    # Load data
    data = load_data(DATA_PATH)

    # Preprocess data
    X_train, X_test, y_train, y_test, vectorizer = preprocess_data(data)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate model
    evaluate_model(model, X_test, y_test)

    # Save model and vectorizer
    save_model(model, vectorizer, MODEL_PATH, VECTORIZER_PATH)

if __name__ == '__main__':
    main()
