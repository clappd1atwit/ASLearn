import cv2
import mediapipe as mp
import numpy as np
import csv
import os
import time

# === Initialize MediaPipe Hands ===
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5)

# === Create directory for saving data ===
data_dir = "sign_language_data"
os.makedirs(data_dir, exist_ok=True)

# === Define ASL alphabet (excluding J and Z) ===
labels = [chr(i) for i in range(65, 91) if chr(i) not in ["J", "Z"]]  # A-Y excluding J and Z

# === CSV file setup ===
data_file = os.path.join(data_dir, "sign_data.csv")

# ✅ Correct header generation (Each x and y coordinate has its own column)
header = ["label"] + [f"x{i}" for i in range(21)] + [f"y{i}" for i in range(21)]

# === Write the header to the CSV file ===
with open(data_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

# === Start video capture ===
cap = cv2.VideoCapture(0)

# === Recording parameters ===
recording_time = 15  # Time in seconds for each letter
break_time = 10       # Pause between letters

for label in labels:
    print(f"Get ready to sign: {label}")
    time.sleep(2)  # Short preparation time

    start_time = time.time()
    while time.time() - start_time < recording_time:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract x and y coordinates for all 21 landmarks
                keypoints = []
                for lm in hand_landmarks.landmark:
                    keypoints.append(lm.x)
                    keypoints.append(lm.y)

                # Save keypoints to CSV
                with open(data_file, mode='a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([label] + keypoints)

        # Display the current letter on the screen
        cv2.putText(frame, f"Sign: {label}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Sign Language Data Collection", frame)

        # Quit early if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

    print(f"Completed {label}. Taking a short break...\n")
    time.sleep(break_time)  # Short break before the next letter

cap.release()
cv2.destroyAllWindows()
print("Data collection complete!")
