import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os

# Path to the CSV file
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
csv_file_path = os.path.join(desktop, "HandGestureData", "gesture_data.csv")

# Output directory for processed data
output_dir = os.path.join(desktop, "ProcessedData")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load data
print("Loading data...")
data = pd.read_csv(csv_file_path)

# Separate features (landmarks) and labels
X = data.iloc[:, 1:].values  # Landmark features
y = data.iloc[:, 0].values   # Labels

# Filter out unwanted labels ('P', 'Q', 'J', 'Z')
print("Filtering unwanted labels...")
unwanted_labels = {'P', 'Q', 'J', 'Z'}
data = data[~data.iloc[:, 0].isin(unwanted_labels)]
X = data.iloc[:, 1:].values
y = data.iloc[:, 0].values

# Normalize landmark coordinates (0-1 range)
print("Normalizing data...")
X_normalized = X / X.max(axis=0)

# Dynamically encode labels (based on present labels)
print("Encoding labels...")
present_labels = sorted(set(y))  # Identify the remaining labels
label_to_int = {label: idx for idx, label in enumerate(present_labels)}

# Display label mapping for reference
print("Label mapping:", label_to_int)

y_encoded = np.array([label_to_int[label] for label in y])

# Split data into training and validation sets
print("Splitting data...")
X_train, X_val, y_train, y_val = train_test_split(X_normalized, y_encoded, test_size=0.2, random_state=42)

# Save processed data
print("Saving processed data...")
np.save(os.path.join(output_dir, "X_train.npy"), X_train)
np.save(os.path.join(output_dir, "X_val.npy"), X_val)
np.save(os.path.join(output_dir, "y_train.npy"), y_train)
np.save(os.path.join(output_dir, "y_val.npy"), y_val)

# Save label mapping for later use
label_mapping_path = os.path.join(output_dir, "label_mapping.npy")
np.save(label_mapping_path, label_to_int)

print(f"Processed data saved to {output_dir}")
print(f"Label mapping saved to {label_mapping_path}")
