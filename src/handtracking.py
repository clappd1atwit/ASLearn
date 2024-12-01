import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model
import os

def main():
    # Load the trained model
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    model_path = os.path.join(desktop, "ProcessedData", "gesture_recognition_model.h5")
    model = load_model(model_path)
    print(f"Model loaded from {model_path}")

    # Map numeric labels back to letters
    label_map = {i: chr(65 + i) for i in range(26)}  # 0 -> A, 1 -> B, ..., 25 -> Z
    confidence_threshold = 0.95  # Minimum confidence to display a gesture

    # Initialize MediaPipe Hands
    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands()
    mp_drawing = mp.solutions.drawing_utils

    # Initialize OpenCV
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Gesture Recognition", cv2.WINDOW_NORMAL)

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.resizeWindow('Gesture Recognition', frame_width, frame_height)

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
        text = ''

        # If hands are detected, extract landmarks and make predictions
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, landmarks, mp_hand.HAND_CONNECTIONS)

                # Collect landmark data
                landmark_list = []
                for lm in landmarks.landmark:
                    landmark_list.extend([lm.x, lm.y, lm.z])  # Flatten x, y, z into a single list

                # Convert to numpy array and reshape for prediction
                input_data = np.array(landmark_list).reshape(1, -1)
                input_data = input_data / np.max(input_data)  # Normalize, if needed
                prediction = model.predict(input_data)
                predicted_prob = np.max(prediction)  # Highest probability
                predicted_label = np.argmax(prediction)  # Get the label with the highest probability
                

                # Only display gesture if confidence is above the threshold
                if predicted_prob > confidence_threshold:
                    text = label_map[predicted_label]
                    print(f"Predicted: {text}, Confidence: {predicted_prob}")
                else:
                    text = "No gesture detected"

        # Display predicted gesture on the frame
        cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
        cv2.imshow("Gesture Recognition", frame)

        # Exit when 'q' key is pressed or window is x'ed out
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or cv2.getWindowProperty('Gesture Recognition', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

#ORIGINAL 
#import cv2
# import mediapipe as mp
# import os

# from helpers.helpers import *
# from letters import *

# def main():
#     # Create a directory on the desktop to save captured frames -- TESTING 
#     desktop = os.path.join(os.path.expanduser("~"), "Desktop")
#     save_dir = os.path.join(desktop, "CapturedFrames")
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)

#     mp_hand = mp.solutions.hands
#     hands = mp_hand.Hands()
#     mp_drawing = mp.solutions.drawing_utils

#     cap = cv2.VideoCapture(0)
    
#     cv2.namedWindow("Free Mode", cv2.WINDOW_NORMAL)
    
#     frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     cv2.resizeWindow('Free Mode', frame_width, frame_height)

#     font = cv2.FONT_HERSHEY_SIMPLEX
#     font_scale = 3
#     font_thickness = 4
#     text_position_left = (10, 80)
#     color = (255, 50, 255)

#     frame_counter = 0  # Counter for naming saved frames

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture frame")
#             break

#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         results = hands.process(rgb_frame)
#         text = ''
        
#         # If hands are detected, draw landmarks on the frame
#         if results.multi_hand_landmarks:
#             for landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(frame, landmarks, mp_hand.HAND_CONNECTIONS)
                
#                 if is_letter_a(results, landmarks):
#                     text = 'A'
#                 elif is_letter_b(results, landmarks):
#                     text = 'B'
#                 elif is_letter_c(results, landmarks):
#                     text = 'C'
#                 elif is_letter_d(results, landmarks):
#                     text = 'D'
#                 elif is_letter_e(results, landmarks):
#                     text = 'E'
#                 elif is_letter_f(results, landmarks):
#                     text = 'F'
#                 elif is_letter_g(results, landmarks):
#                     text = 'G'
#                 elif is_letter_h(results, landmarks):
#                     text = 'H'
#                 elif is_letter_i(results, landmarks):
#                     text = 'I'
#                 elif is_letter_j(results, landmarks):
#                     text = 'J'
#                 elif is_letter_k(results, landmarks):
#                     text = 'K'
#                 elif is_letter_l(results, landmarks):
#                     text = 'L'
#                 elif is_letter_m(results, landmarks):
#                     text = 'M'
#                 elif is_letter_n(results, landmarks):
#                     text = 'N'
#                 elif is_letter_o(results, landmarks):
#                     text = 'O'
#                 elif is_letter_p(results, landmarks):
#                     text = 'P'
#                 elif is_letter_q(results, landmarks):
#                     text = 'Q'
#                 elif is_letter_r(results, landmarks):
#                     text = 'R'
#                 elif is_letter_t(results, landmarks):
#                     text = 'T'
#                 elif is_letter_s(results, landmarks):
#                     text = 'S'
#                 elif is_letter_u(results, landmarks):
#                     text = 'U'
#                 elif is_letter_v(results, landmarks):
#                     text = 'V'
#                 elif is_letter_w(results, landmarks):
#                     text = 'W'
#                 elif is_letter_x(results, landmarks):
#                     text = 'X'
#                 elif is_letter_y(results, landmarks):
#                     text = 'Y'
#                 elif is_letter_z(results, landmarks):
#                     text = 'Z'
                
#         cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
#         cv2.imshow("Free Mode", frame)

#         # Exit when 'q' key is pressed or window is x'ed out
#         key = cv2.waitKey(1) & 0xFF
#         if key == ord('q') or cv2.getWindowProperty('Free Mode', cv2.WND_PROP_VISIBLE) < 1:
#             break
#         elif key == ord('c'):  # Save the current frame
#             frame_filename = os.path.join(save_dir, f"frame_{frame_counter:04d}.png")
#             cv2.imwrite(frame_filename, frame)
#             print(f"Frame saved: {frame_filename}")
#             frame_counter += 1

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()
