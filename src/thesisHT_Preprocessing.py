import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import layers, models
import os

# Load the data
data_file = "sign_language_data/sign_data.csv"
# Reload CSV
df = pd.read_csv('sign_language_data/sign_data.csv')

# Drop NaNs (Optional)
# df = df.dropna()

# Split features and labels
X = df.drop('label', axis=1).values
y = df['label'].values

# Encode labels
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Save the label encoder to file
with open('label_encoder.pkl', 'wb') as le_file:
    pickle.dump(label_encoder, le_file)

print("Label encoder saved as 'label_encoder.pkl'")

# Normalize keypoints (optional)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Save the scaler
with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("Scaler saved as 'scaler.pkl'")

# Train/test split
from sklearn.model_selection import train_test_split
# Split first
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_encoded, test_size=0.2, random_state=42
)

# Confirm shapes BEFORE reshaping
print(X_train.shape, y_train.shape)

# Now reshape for CNN
X_train_cnn = X_train.reshape(-1, 21, 2, 1)
X_test_cnn = X_test.reshape(-1, 21, 2, 1)

# Confirm shapes AFTER reshaping
print(X_train_cnn.shape, y_train.shape)

# Check matching lengths
assert X_train_cnn.shape[0] == y_train.shape[0], "Mismatch!"
assert X_test_cnn.shape[0] == y_test.shape[0], "Mismatch!"



#CNN MODEL

# Define the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 2), activation='relu', input_shape=(21, 2, 1)),
    layers.MaxPooling2D((2, 1)),
    layers.Conv2D(64, (3, 1), activation='relu'),
    layers.MaxPooling2D((2, 1)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(len(np.unique(y_train)), activation='softmax')  # 24 classes for A-Y (excluding J, Z)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# Train the model
history = model.fit(X_train_cnn, y_train, epochs=30, batch_size=32,
                    validation_data=(X_test_cnn, y_test))

# Evaluate on test set
test_loss, test_acc = model.evaluate(X_test_cnn, y_test)
print(f"Test Accuracy: {test_acc:.2f}")

import matplotlib.pyplot as plt

# Accuracy plot
plt.plot(history.history['accuracy'], label='train_acc')
plt.plot(history.history['val_accuracy'], label='val_acc')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Loss plot
plt.plot(history.history['loss'], label='train_loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()


# Save the trained model
model.save("asl_keypoint_cnn.h5")

print("Model saved successfully!")


# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# import os

# # Path to the CSV file
# desktop = os.path.join(os.path.expanduser("~"), "Desktop")
# csv_file_path = os.path.join(desktop, "HandGestureData", "gesture_data.csv")

# # Output directory for processed data
# output_dir = os.path.join(desktop, "ProcessedData")
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# # Load data
# print("Loading data...")
# data = pd.read_csv(csv_file_path)

# # Separate features (landmarks) and labels
# X = data.iloc[:, 1:].values  # Landmark features
# y = data.iloc[:, 0].values   # Labels

# # Filter out unwanted labels ('P', 'Q', 'J', 'Z')
# print("Filtering unwanted labels...")
# unwanted_labels = {'P', 'Q', 'J', 'Z'}
# data = data[~data.iloc[:, 0].isin(unwanted_labels)]
# X = data.iloc[:, 1:].values
# y = data.iloc[:, 0].values

# # Normalize landmark coordinates (0-1 range)
# print("Normalizing data...")
# X_normalized = X / X.max(axis=0)

# # Dynamically encode labels (based on present labels)
# print("Encoding labels...")
# present_labels = sorted(set(y))  # Identify the remaining labels
# label_to_int = {label: idx for idx, label in enumerate(present_labels)}

# # Display label mapping for reference
# print("Label mapping:", label_to_int)

# y_encoded = np.array([label_to_int[label] for label in y])

# # Split data into training and validation sets
# print("Splitting data...")
# X_train, X_val, y_train, y_val = train_test_split(X_normalized, y_encoded, test_size=0.2, random_state=42)

# # Save processed data
# print("Saving processed data...")
# np.save(os.path.join(output_dir, "X_train.npy"), X_train)
# np.save(os.path.join(output_dir, "X_val.npy"), X_val)
# np.save(os.path.join(output_dir, "y_train.npy"), y_train)
# np.save(os.path.join(output_dir, "y_val.npy"), y_val)

# # Save label mapping for later use
# label_mapping_path = os.path.join(output_dir, "label_mapping.npy")
# np.save(label_mapping_path, label_to_int)

# print(f"Processed data saved to {output_dir}")
# print(f"Label mapping saved to {label_mapping_path}")
