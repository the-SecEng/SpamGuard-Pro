# File: load_dataset.py
import pandas as pd


file_path = "./datasets/SMSSpamCollection"

# Define column names
columns = ['label', 'message']

# Read the dataset into a DataFrame
df = pd.read_csv(file_path, sep='\t', names=columns)
