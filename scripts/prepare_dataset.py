import os
import pandas as pd

def read_emails(directory, label):
    emails = []
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        content = file.read()
                        if content.strip():  # Ensure the file is not empty
                            emails.append((content, label))
                        else:
                            print(f"Skipping empty file: {file_path}")
                except PermissionError as e:
                    print(f"Permission error: {e} for file {file_path}")
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
            else:
                print(f"Skipping non-file: {file_path}")
    return emails

# Read ham and spam emails
ham_emails = read_emails('data/easy_ham', 0)  # 0 for ham
spam_emails = read_emails('data/spam', 1)     # 1 for spam

# Combine the datasets and create a DataFrame
emails = ham_emails + spam_emails
df = pd.DataFrame(emails, columns=['text', 'label'])

# Print a sample of the DataFrame and check its size
print(df.head())
print(f"Number of rows in the DataFrame: {len(df)}")

# Save the DataFrame to a CSV file
os.makedirs('data', exist_ok=True)
df.to_csv('data/spam_data.csv', index=False)

print("Dataset prepared and saved successfully.")
