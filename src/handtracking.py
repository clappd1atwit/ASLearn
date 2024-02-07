import cv2
import mediapipe as mp

from helpers import *
from letters import *

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
                
                text = ''
                if is_letter_a(results, landmarks):
                    text = 'A'
                elif is_letter_b(results, landmarks):
                    text = 'B'
                elif is_letter_d(results, landmarks):
                    text = 'D'
                
                cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
                

        cv2.imshow("Hand Tracking", frame)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
