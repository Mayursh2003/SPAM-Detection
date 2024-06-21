import pandas as pd
import numpy as np
import random

# Function to generate random text
def generate_text(spam=True):
    spam_texts = [
        "Free entry in a weekly competition!", "Win cash prizes now!!!",
        "Congratulations! You've won a free ticket.", "Exclusive offer just for you!",
        "Claim your free reward today!", "You have been selected for a special prize!"
    ]
    ham_texts = [
        "Hey, are we still on for dinner tonight?", "Can you send me the report by EOD?",
        "Meeting rescheduled to 3 PM.", "Looking forward to seeing you!",
        "Happy birthday! Hope you have a great day!", "Don't forget about the meeting tomorrow."
    ]
    return random.choice(spam_texts) if spam else random.choice(ham_texts)

# Generate sample data
num_samples = 500
data = {
    'id': range(1, num_samples + 1),
    'text': [generate_text(spam=bool(random.getrandbits(1))) for _ in range(num_samples)],
    'label': [random.randint(0, 1) for _ in range(num_samples)],
    'feature_0': np.random.rand(num_samples),
    'feature_1': np.random.rand(num_samples),
    'feature_2': np.random.rand(num_samples)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('/data/spam_data1.csv', index=False)

print("Sample CSV file with 500 lines created successfully.")
