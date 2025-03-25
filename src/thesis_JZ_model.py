import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import pickle

# === Step 1: Load Preprocessed Data ===
X_train = np.load("X_dynamic_train.npy")
X_test = np.load("X_dynamic_test.npy")
y_train = np.load("y_dynamic_train.npy")
y_test = np.load("y_dynamic_test.npy")

print("Loaded dynamic training data:")
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

# === Step 2: Build CNN + LSTM Model ===
model = models.Sequential([
    layers.TimeDistributed(layers.Conv1D(64, 3, activation='relu'), input_shape=(30, 42, 1)),
    layers.TimeDistributed(layers.MaxPooling1D(2)),
    layers.TimeDistributed(layers.Flatten()),
    layers.LSTM(64, return_sequences=False),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(len(np.unique(y_train)), activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# === Step 3: Reshape Input for CNN + LSTM ===
# (samples, sequence_len, features) -> (samples, sequence_len, features, 1)
X_train = X_train.reshape((X_train.shape[0], 50, 42, 1))
X_test = X_test.reshape((X_test.shape[0], 50, 42, 1))

# === Step 4: Train Model ===
history = model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=16,
    validation_data=(X_test, y_test)
)

# === Step 5: Evaluate and Save Model ===
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc:.4f}")

model.save("dynamic_sign_model.h5")
print("Model saved as 'dynamic_sign_model.h5'")

# === Step 6: Plot Training Performance ===
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.title('Dynamic Gesture Training Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.title('Dynamic Gesture Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()
