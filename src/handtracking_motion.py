import cv2
import mediapipe as mp

from collections import deque
from helpers import *
from letters import *

def detect_z(index_hand_landmarks):
    # Filter out None values
    index_hand_landmarks = [point for point in index_hand_landmarks if point is not None]

    # Check if there are enough points to analyze
    if len(index_hand_landmarks) < 3:
        return False

    # Extract x and y coordinates of the points
    x_values = [point[0] for point in index_hand_landmarks]
    y_values = [point[1] for point in index_hand_landmarks]

    # Find corners (significant changes in direction)
    corners = []
    for i in range(1, len(index_hand_landmarks) - 1):
        dx1 = x_values[i] - x_values[i-1]
        dy1 = y_values[i] - y_values[i-1]
        dx2 = x_values[i+1] - x_values[i]
        dy2 = y_values[i+1] - y_values[i]
        if dx1 is not None and dy1 is not None and dx2 is not None and dy2 is not None:
            angle = abs(dx1*dx2 + dy1*dy2) / ((dx1**2 + dy1**2)**0.5 * (dx2**2 + dy2**2)**0.5)
            if angle < 0.8:  # Tune this threshold based on your requirements
                corners.append((x_values[i], y_values[i]))

    # Check if corners form the shape of a 'Z'
    if len(corners) >= 2:
        start = (x_values[0], y_values[0])
        end = (x_values[-1], y_values[-1])
        first_corner = corners[0]
        last_corner = corners[-1]

        # Check if corners are aligned with the start and end points
        if (start[1] < first_corner[1]) and (end[1] < last_corner[1]):
            return True

    return False

def main():
    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_thickness = 4
    text_position_left = (10, 80)
    color = (255, 50, 255)

    # Queue to store locations of index finger tip for the last 150 frames
    index_finger_tip_locations = deque(maxlen=50)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        # If hands are detected, draw landmarks on the frame and store index finger tip location
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)

                # Get index finger tip location
                index_finger_tip = hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP]
                image_height, image_width, _ = frame.shape
                index_finger_tip_x = int(index_finger_tip.x * image_width)
                index_finger_tip_y = int(index_finger_tip.y * image_height)

                # Store index finger tip location
                index_finger_tip_locations.append((index_finger_tip_x, index_finger_tip_y))
        else:
            index_finger_tip_locations.append((None, None))

        # Draw index finger tip locations from the last 50 frames
        for x, y in index_finger_tip_locations:
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            
        text = ''
        
        if detect_z(index_finger_tip_locations):
            text = 'Z'
        
        cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
        cv2.imshow("Hand Tracking", frame)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
