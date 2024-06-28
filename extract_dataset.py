import tarfile
import os

# Define paths to the tar.bz2 files
ham_path = 'data/20021010_easy_ham.tar.bz2'
spam_path = 'data/20021010_spam.tar.bz2'

# Function to extract tar.bz2 files
def extract_tar_bz2(file_path, extract_path):
    with tarfile.open(file_path, 'r:bz2') as tar:
        tar.extractall(path=extract_path)

# Extract the datasets
extract_tar_bz2(ham_path, 'data/easy_ham')
extract_tar_bz2(spam_path, 'data/spam')

print("Extraction complete.")
