import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load the dataset
df = pd.read_csv('data/spam_data.csv')

# Ensure the DataFrame is not empty
if df.empty:
    raise ValueError("The DataFrame is empty. Ensure the data preparation step was successful.")

# Ensure the text column is not empty
if df['text'].isnull().sum() > 0 or df['text'].str.strip().eq('').sum() > 0:
    raise ValueError("The text column contains empty or null values.")

# Vectorize the text data
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])

# Train the model
y = df['label']
model = RandomForestClassifier()
model.fit(X, y)

# Save the model and vectorizer
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/spam_classifier.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')

print("Model trained and saved successfully.")
