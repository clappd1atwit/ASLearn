import mediapipe as mp
import cv2

mp_hand = mp.solutions.hands
hands = mp_hand.Hands()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cv2.namedWindow("Hand Calibration", cv2.WINDOW_NORMAL)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cv2.resizeWindow('Hand Calibration', frame_width, frame_height)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
font_thickness = 2
text_position_left = (10, 80)
color = (255, 50, 255)

wait_frames = 0

while cap.isOpened():
    text = "Hold up your RIGHT hand facing forward" #TODO: Fix this, text gets cut off on screen
    
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = hands.process(rgb_frame) # Mediapipe hand landmarks
    
    if results.multi_hand_landmarks:
        for landmark in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, landmark, mp_hand.HAND_CONNECTIONS)
        
        if len(results.multi_hand_landmarks) > 1:
            text = 'Too many hands present'
            wait_frames = 0

        # Give user time to hold up hand on screen
        elif wait_frames < 50:
            wait_frames += 1
            
        else:
            pass #TODO: write the code to determine the hand and save to config file
    
    else:
        wait_frames = 0
        
    cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
    cv2.imshow("Hand Calibration", frame)

            # Exit when 'q' key is pressed or window is x'ed out
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Hand Calibration', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()