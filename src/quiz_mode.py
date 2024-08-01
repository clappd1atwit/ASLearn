import cv2
import random
import time
import mediapipe as mp

from helpers.helpers import *
from letters import *
from modules.letter_modules import *


# Pick 10 random letters from the alphabet to quiz the user on
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'] # No 'j' or 'z'
random.shuffle(alphabet)
quiz_letters = alphabet[:10]

def run_quiz():
    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    
    cv2.namedWindow("Quiz Mode", cv2.WINDOW_NORMAL)
    
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.resizeWindow('Quiz Mode', frame_width, frame_height)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2.5
    font_thickness = 3
    text_position_left = (10, 80)
    text_position_right = (frame_width - 140, 80)
    
    idle_color = (255, 50, 255)
    correct_color = (0, 200, 0)
    incorrect_color = (0, 0, 200)
    color = idle_color
    
    timer_length = 5

    counter = 0
    hold_correct = False
    hold_counter = 0
    hold_incorrect = False
    
    start_time = time.time()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)
        
        text = quiz_letters[counter].upper()
        elapsed_time = timer_length - int(time.time() - start_time)
        time_text = str(elapsed_time)
        
        if elapsed_time < 1:
            text = quiz_letters[counter].upper() + ' INCORRECT'
            color = incorrect_color
            hold_incorrect = True
            
        if hold_incorrect:
            text = quiz_letters[counter].upper() + ' INCORRECT'
            hold_counter += 1
            time_text = '' 
            
        if hold_counter > 15:
            counter += 1
            hold_counter = 0
            hold_correct = False
            hold_incorrect = False
            color = idle_color
            time_text = ''
            start_time = time.time()
            
        if hold_correct:
            text = quiz_letters[counter].upper() + ' CORRECT'
            hold_counter += 1
            time_text = ''

        # If hands are detected, draw landmarks on the frame
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, landmarks, mp_hand.HAND_CONNECTIONS)  
            
            if letter_functions[quiz_letters[counter]](results, landmarks):
                color = correct_color
                text = quiz_letters[counter].upper() + ' CORRECT'
                hold_correct = True
                
                
        cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
        cv2.putText(frame, time_text, text_position_right, font, font_scale, idle_color, font_thickness)
        cv2.imshow("Quiz Mode", frame)

        if counter >= 10:
            break

        # Exit when 'q' key is pressed or window is x'ed out
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Quiz Mode', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_quiz()