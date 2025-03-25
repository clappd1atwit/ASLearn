import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
import pickle
from collections import deque

# Load the trained dynamic model
model = tf.keras.models.load_model("dynamic_sign_model.h5")

# Load label encoder
with open("dynamic_label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Setup buffer for 50-frame sliding window
SEQUENCE_LENGTH = 50
keypoint_window = deque(maxlen=SEQUENCE_LENGTH)

# Start webcam
cap = cv2.VideoCapture(0)

print("Real-time dynamic recognition running... Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            keypoints = []
            for lm in hand_landmarks.landmark:
                keypoints.extend([lm.x, lm.y])

            keypoint_window.append(keypoints)

            # Predict when we have enough frames
            if len(keypoint_window) == SEQUENCE_LENGTH:
                input_sequence = np.array(keypoint_window).reshape(1, SEQUENCE_LENGTH, 42, 1)
                prediction = model.predict(input_sequence, verbose=0)
                predicted_index = np.argmax(prediction)
                predicted_label = label_encoder.inverse_transform([predicted_index])[0]
                confidence = np.max(prediction)

                if confidence > 0.8:  # Optional: confidence threshold
                    cv2.putText(frame, f"Predicted: {predicted_label} ({confidence:.2f})",
                                (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    else:
        keypoint_window.clear()  # Reset if hand not visible

    cv2.imshow("Dynamic ASL J/Z Recognizer", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
