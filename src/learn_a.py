import cv2
import mediapipe as mp

from helpers import *
from letters import *
import hand_colors

def main():
    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    
    cv2.namedWindow("Hand Tracking", cv2.WINDOW_NORMAL)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_thickness = 4
    text_position_left = (10, 80)
    color = (255, 50, 255)
    
    ret, frame = cap.read()
    
    landmarks_color = hand_colors.get_incorrect_hand_landmarks_style()
    connections_color = hand_colors.get_incorrect_hand_connections_style()

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
                mp_drawing.draw_landmarks(frame, landmarks, mp_hand.HAND_CONNECTIONS, landmarks_color, connections_color)

                color = (255, 50, 255)
                text = 'A'
                wrist = wrist_lm(landmarks)
                
                thumb_tip = thumb_tip_lm(landmarks)
                thumb_mcp = thumb_mcp_lm(landmarks)
    
                index_mcp = index_mcp_lm(landmarks)
                index_dip = index_dip_lm(landmarks)
                index_pip = index_pip_lm(landmarks)
                index_tip = index_tip_lm(landmarks)
                
                middle_pip = middle_pip_lm(landmarks)
                middle_tip = middle_tip_lm(landmarks)
                
                ring_pip = ring_pip_lm(landmarks)
                ring_tip = ring_tip_lm(landmarks)
                
                pinky_pip = pinky_pip_lm(landmarks)
                pinky_tip = pinky_tip_lm(landmarks)
                
                index_closed = not is_finger_open(index_tip, index_pip, wrist)
                middle_closed = not is_finger_open(middle_tip, middle_pip, wrist)
                ring_closed = not is_finger_open(ring_tip, ring_pip, wrist)
                pinky_closed = not is_finger_open(pinky_tip, pinky_pip, wrist)
                
                handedness = is_right_hand(results, landmarks)
                
                if is_letter_a(results, landmarks):
                    text = 'A - Correct!'
                    color = (0, 200, 0)
                    landmarks_color = hand_colors.get_correct_hand_landmarks_style()
                    connections_color = hand_colors.get_correct_hand_connections_style()

                else:
                    hand_colors.get_incorrect_hand_landmarks_style()
                    hand_colors.get_incorrect_hand_connections_style()

                    if is_facing_forward(results, landmarks):
                        hand_colors.set_palm_color(hand_colors._GREEN)
                    if ((handedness and thumb_tip.x > max(index_mcp.x, index_dip.x) and 
                        (normalized_slope(thumb_mcp, thumb_tip) > .7 or
                        normalized_slope(thumb_mcp, thumb_tip) < -.7)) or 
                        (not handedness and thumb_tip.x < min(index_mcp.x, index_dip.x) and 
                        (normalized_slope(thumb_mcp, thumb_tip) > .7 or
                        normalized_slope(thumb_mcp, thumb_tip) < -.7))):
                        hand_colors.set_thumb_color(hand_colors._GREEN)
                    if index_closed:
                        hand_colors.set_index_color(hand_colors._GREEN)
                    if middle_closed:
                        hand_colors.set_middle_color(hand_colors._GREEN)
                    if ring_closed:
                        hand_colors.set_ring_color(hand_colors._GREEN)
                    if pinky_closed:
                        hand_colors.set_pinky_color(hand_colors._GREEN)
                    landmarks_color = hand_colors.get_current_hand_landmarks_style()
                    connections_color = hand_colors.get_current_hand_connections_style()
                    
                
                cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
        cv2.imshow("Hand Tracking", frame)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
