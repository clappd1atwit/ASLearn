import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
import pickle
import time  # <-- added

# === Step 1: Load Trained Model and Preprocessing Tools ===
model = tf.keras.models.load_model('asl_keypoint_cnn.h5')

# Load label encoder
with open('label_encoder.pkl', 'rb') as le_file:
    label_encoder = pickle.load(le_file)

# Load scaler
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# === Step 2: Initialize MediaPipe Hands ===
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)

# === Step 3: Start Webcam Capture ===
cap = cv2.VideoCapture(0)
prev_time = time.time()  # <-- Track time for FPS

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    prediction_text = ""

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            keypoints = []
            for lm in hand_landmarks.landmark:
                keypoints.append(lm.x)
                keypoints.append(lm.y)

            # Convert keypoints to numpy array and reshape for scaler
            keypoints_np = np.array(keypoints).reshape(1, -1)

            # Scale keypoints using the same scaler from training
            keypoints_scaled = scaler.transform(keypoints_np)

            # Reshape for CNN prediction
            keypoints_cnn = keypoints_scaled.reshape(-1, 21, 2, 1)

            # Make prediction
            prediction = model.predict(keypoints_cnn)
            predicted_class = np.argmax(prediction)
            predicted_letter = label_encoder.inverse_transform([predicted_class])[0]

            prediction_text = f"Prediction: {predicted_letter} ({prediction[0][predicted_class]:.2f})"

    # === Calculate FPS ===
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # Display prediction and FPS on screen
    cv2.putText(frame, prediction_text, (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow("ASL Real-Time Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
