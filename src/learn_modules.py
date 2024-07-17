import sys
import cv2
import mediapipe as mp
import argparse

from helpers.helpers import *
from letters import *
from modules.letter_modules import *
import helpers.hand_colors as hand_colors

def letter_is_dynamic(letter):
    return letter == 'j' or letter == 'z'

def run_module(letter):
    if letter_is_dynamic(letter):
        letter_modules[letter](None, None)
    else:
        run_static_module(letter)

def run_static_module(letter):
    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    
    cv2.namedWindow("Learn Module", cv2.WINDOW_NORMAL)
    
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.resizeWindow('Learn Module', frame_width, frame_height)


    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_thickness = 4
    text_position_left = (10, 80)
    text_color = (255, 50, 255)
    
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
            for lms in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, lms, mp_hand.HAND_CONNECTIONS, landmarks_color, connections_color)
                
                text, text_color, landmarks_color, connections_color = letter_modules[letter](results, lms)    
                
        cv2.putText(frame, text, text_position_left, font, font_scale, text_color, font_thickness)
        cv2.imshow("Learn Module", frame)

        # Exit when 'q' key is pressed or window is x'ed out
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Learn Module', cv2.WND_PROP_VISIBLE) < 1:
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="runs a learning module for a specified letter")
    parser.add_argument("letter", help="Specify a letter as an argument")
    args = parser.parse_args()

    if len(args.letter) != 1 or not args.letter.isalpha():
        print("ERROR: letter argument must be a single alphabetical character")
        sys.exit(1)

    run_module(args.letter.lower())