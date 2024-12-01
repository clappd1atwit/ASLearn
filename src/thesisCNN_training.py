import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report
import os

# Path to processed data and label mapping
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
processed_data_path = os.path.join(desktop, "ProcessedData")

# Load preprocessed data
print("Loading preprocessed data...")
X_train = np.load(os.path.join(processed_data_path, "X_train.npy"))
X_val = np.load(os.path.join(processed_data_path, "X_val.npy"))
y_train = np.load(os.path.join(processed_data_path, "y_train.npy"))
y_val = np.load(os.path.join(processed_data_path, "y_val.npy"))

# Load the label mapping
print("Loading label mapping...")
label_mapping_path = os.path.join(processed_data_path, "label_mapping.npy")
label_to_int = np.load(label_mapping_path, allow_pickle=True).item()
int_to_label = {v: k for k, v in label_to_int.items()}  # Reverse the mapping

# Display the label mapping for verification
print("Label Mapping:", label_to_int)

# One-hot encode labels
print("One-hot encoding labels...")
num_classes = len(label_to_int)  # Number of classes matches the mapping
y_train = to_categorical(y_train, num_classes)
y_val = to_categorical(y_val, num_classes)


model = Sequential([
    Dense(256, activation='relu', input_shape=(X_train.shape[1],)),
    BatchNormalization(),
    Dropout(0.3),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(num_classes, activation='softmax')
])
# # Define the CNN model
# print("Building model...")
# model = Sequential([
#     Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
#     Dropout(0.2),
#     Dense(64, activation='relu'),
#     Dropout(0.2),
#     Dense(num_classes, activation='softmax')  # Output layer
# ])

# Compile the model
print("Compiling model...")
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
print("Training model...")
history = model.fit(X_train, y_train,
                    epochs=50,
                    batch_size=32,
                    validation_data=(X_val, y_val))

# Evaluate the model
print("Evaluating model...")
test_loss, test_accuracy = model.evaluate(X_val, y_val)
print(f"Validation Accuracy: {test_accuracy}")

# Generate a classification report
print("Generating classification report...")
y_pred = model.predict(X_val)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_val, axis=1)

# Map indices back to letter labels for the report
target_names = [int_to_label[i] for i in range(num_classes)]
valid_labels = list(range(num_classes))  # Ensure labels match the number of classes

print("\nClassification Report:")
print(classification_report(y_true_classes, y_pred_classes, target_names=target_names, labels=valid_labels))

# Save the trained model
model_save_path = os.path.join(processed_data_path, "gesture_recognition_model.h5")
model.save(model_save_path)
print(f"Model saved to {model_save_path}")

# import numpy as np
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout
# from tensorflow.keras.utils import to_categorical
# from sklearn.metrics import classification_report
# import os

# # Path to processed data
# desktop = os.path.join(os.path.expanduser("~"), "Desktop")
# processed_data_path = os.path.join(desktop, "ProcessedData")

# # Load preprocessed data
# print("Loading preprocessed data...")
# X_train = np.load(os.path.join(processed_data_path, "X_train.npy"))
# X_val = np.load(os.path.join(processed_data_path, "X_val.npy"))
# y_train = np.load(os.path.join(processed_data_path, "y_train.npy"))
# y_val = np.load(os.path.join(processed_data_path, "y_val.npy"))

# # One-hot encode labels
# print("One-hot encoding labels...")
# num_classes = len(np.unique(y_train))+1  # Number of unique gestures (A-Z = 26) CHANGE WHEN DOING ALL LETTERS - ELIM(+1)
# print(np.unique(y_train))
# y_train = to_categorical(y_train, num_classes)
# y_val = to_categorical(y_val, num_classes)

# # Define the CNN model
# print("Building model...")
# model = Sequential([
#     Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
#     Dropout(0.2),
#     Dense(64, activation='relu'),
#     Dropout(0.2),
#     Dense(num_classes, activation='softmax')  # Output layer
# ])

# # Compile the model
# print("Compiling model...")
# model.compile(optimizer='adam',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])

# # Train the model
# print("Training model...")
# history = model.fit(X_train, y_train,
#                     epochs=50,
#                     batch_size=32,
#                     validation_data=(X_val, y_val))

# # Evaluate the model
# print("Evaluating model...")
# test_loss, test_accuracy = model.evaluate(X_val, y_val)
# print(f"Validation Accuracy: {test_accuracy}")

# # Generate a classification report
# y_pred = model.predict(X_val)
# y_pred_classes = np.argmax(y_pred, axis=1)
# y_true_classes = np.argmax(y_val, axis=1)

# print("\nClassification Report:")
# print(classification_report(y_true_classes, y_pred_classes, target_names=[chr(i + 65) for i in range(num_classes-3)]))

# # Save the trained model
# model_save_path = os.path.join(processed_data_path, "gesture_recognition_model.h5")
# model.save(model_save_path)
# print(f"Model saved to {model_save_path}")
