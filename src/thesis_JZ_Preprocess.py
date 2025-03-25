import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

# === Settings ===
DATA_PATH = "dynamic_sign_data"
SEQUENCE_LENGTH = 50
NUM_KEYPOINTS = 42  # 21 landmarks * (x, y)

# === Load sequences and labels ===
sequences = []
labels = []

for label in os.listdir(DATA_PATH):
    label_path = os.path.join(DATA_PATH, label)
    for file in os.listdir(label_path):
        file_path = os.path.join(label_path, file)
        sequence = np.load(file_path)
        if sequence.shape == (SEQUENCE_LENGTH, NUM_KEYPOINTS):
            sequences.append(sequence)
            labels.append(label)
        else:
            print(f"Skipped {file_path} due to shape {sequence.shape}")


sequences = np.array(sequences)
labels = np.array(labels)

print("Total sequences:", len(sequences))
print("Labels:", np.unique(labels))

# === Encode labels ===
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(labels)

# Save label encoder
with open("dynamic_label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

# === Train/Test split ===
X_train, X_test, y_train, y_test = train_test_split(
    sequences, y_encoded, test_size=0.2, random_state=7
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

# === Save the preprocessed data ===
np.save("X_dynamic_train.npy", X_train)
np.save("X_dynamic_test.npy", X_test)
np.save("y_dynamic_train.npy", y_train)
np.save("y_dynamic_test.npy", y_test)

print("Preprocessing complete and saved!")
