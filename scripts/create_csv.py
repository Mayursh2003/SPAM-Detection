import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Sample data
data = {
    'text': [
        "Free money!!! Claim your prize now!",
        "Meeting at 10 AM tomorrow.",
        "Win a free vacation to the Bahamas!",
        "Don't forget our meeting tomorrow.",
        "Congratulations! You've won a free ticket."
    ],
    'label': [
        "spam",
        "not_spam",
        "spam",
        "not_spam",
        "spam"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Vectorize the text data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text']).toarray()

# Convert the vectorized data to a DataFrame
vectorized_df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])

# Combine the original DataFrame with the vectorized data
final_df = pd.concat([df, vectorized_df], axis=1)

# Save the vectorizer for later use
joblib.dump(vectorizer, 'models/vectorizer.pkl')

# Save the final DataFrame to a CSV file
final_df.to_csv('data/spam_data.csv', index=False)

print("CSV file created successfully.")
