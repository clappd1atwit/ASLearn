import cv2
import mediapipe as mp
import numpy as np

def distance(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

def is_hand_open(landmarks):
    # Define the indices for the thumb and index finger landmarks
    wrist = landmarks.landmark[mp.solutions.hands.HandLandmark.WRIST]
    
    index_finger_mcp = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    index_finger_tip = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    
    middle_finger_mcp = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    middle_finger_tip = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    
    ring_finger_mcp = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    ring_finger_tip = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    
    pinky_mcp = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    pinky_tip = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]

    # Calculate the distance between thumb tip and index finger tip
    index_distance = distance(index_finger_mcp, index_finger_tip)
    middle_distance = distance(middle_finger_mcp, middle_finger_tip)
    ring_distance = distance(ring_finger_mcp, ring_finger_tip)
    pinky_distance = distance(pinky_mcp, pinky_tip)
    
    finger_data = np.array([index_distance, middle_distance, ring_distance, pinky_distance])
   
    avg_distance = np.mean(finger_data)
    finger_variance = np.std(finger_data)
    print(finger_variance)

    threshold = distance(wrist, index_finger_mcp) / 2

    return avg_distance > threshold

def main():
    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    font_thickness = 2
    text_position_left = (10, 30)
    text_position_right = (100, 30)
    color = (0, 255, 0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        # If hands are detected, draw landmarks on the frame
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, landmarks, mp_hand.HAND_CONNECTIONS)

                hand_open = is_hand_open(landmarks)

                if hand_open:
                    text = "Open"
                    color = (0, 255, 0)
                else:
                    text = "Closed"
                    color = (0, 0, 255)
                    
                cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
                

        cv2.imshow("Hand Tracking", frame)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
