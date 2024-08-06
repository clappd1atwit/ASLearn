import sys
import argparse

import cv2
import mediapipe as mp

from collections import deque
from helpers.helpers import *
from letters import *

def detect_z(index_hand_landmarks):
    # Filter out None values
    index_hand_landmarks = [point for point in index_hand_landmarks if point[0] is not None and point[1] is not None]

    # Check if there are enough points to analyze
    if len(index_hand_landmarks) < 7:
        return False, []

    # Extract x and y coordinates of the smoothed points
    x_values = [point[0] for point in index_hand_landmarks]
    y_values = [point[1] for point in index_hand_landmarks]

    # Find corners (significant changes in direction)
    corners = []
    corner_indecies = []
    for i in range(3, len(index_hand_landmarks) - 3):
        dx1 = x_values[i] - x_values[i-3]
        dy1 = y_values[i] - y_values[i-3]
        dx2 = x_values[i] - x_values[i+3]
        dy2 = y_values[i] - y_values[i+3]
        if (dx1**2 + dy1**2)**0.5 * (dx2**2 + dy2**2)**0.5 != 0.0: # Avoid division by zero
            angle = (dx1*dx2 + dy1*dy2) / ((dx1**2 + dy1**2)**0.5 * (dx2**2 + dy2**2)**0.5)
            try:
                angle_degrees = math.degrees(math.acos(angle))
            except Exception as e:
                angle_degrees = 180
            if angle_degrees < 70 and (len(corner_indecies) == 0 or i - corner_indecies[-1] > 2):
                corners.append((x_values[i], y_values[i]))
                corner_indecies.append(i)

    # Check if corners form the shape of a 'Z'
    if len(corners) > 2:
        start = (x_values[0], y_values[0])
        end = corners[2]
        first_corner = corners[0]
        last_corner = corners[1]

        # Check if corners are aligned with the start and end points
        if (start[0] > first_corner[0] and start[0] > end[0] and
            start[1] < end[1] and start[1] < last_corner[1] and
            
            first_corner[0] < last_corner[0] and
            first_corner[1] < end[1] and first_corner[1] < last_corner[1] and
            
            last_corner[0] > end[1]):
            return True, corners

    return False, corners

def detect_j(pinky_hand_landmarks):
    # Filter out None values
    pinky_hand_landmarks = [point for point in pinky_hand_landmarks if point[0] is not None and point[1] is not None]

    # Check if there are enough points to analyze
    if len(pinky_hand_landmarks) < 7:
        return False, 0, 0, 0
    
    x_values = [point[0] for point in pinky_hand_landmarks]
    y_values = [point[1] for point in pinky_hand_landmarks]
    
    xc, yc, R = fit_circle(x_values, y_values)
    
    x_values = [point[0] for point in pinky_hand_landmarks if point[1] > yc]
    y_values = [point[1] for point in pinky_hand_landmarks if point[1] > yc]
    
    # Check again if there are enough points to analyze
    if not len(x_values):
        return False, 0, 0, 0
    
    residuals = np.sqrt((x_values - xc)**2 + (y_values - yc)**2) - R
    
    tolerance = 7.0  # Adjust tolerance as needed
    #print(np.average(np.abs(residuals)), np.max(np.abs(residuals)), R)
    is_circle_flag = (len(residuals) > 5 and 
                      np.average(np.abs(residuals)) < tolerance and
                      any(x < xc for x in x_values) and
                      any(x > xc for x in x_values) and
                      R > 70 and R < 150) #and is_circle(x_values, y_values, xc, yc, R)

    return is_circle_flag, xc, yc, R

def run_module_z(lms):
    pass

def run_module_j():
    pass


letter_modules = {
    'j' : run_module_j,
    'z' : run_module_z,
}

def run_motion_module(letter):
    mp_hand = mp.solutions.hands
    hands = mp_hand.Hands()
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    font_thickness = 4
    text_position_left = (10, 80)
    color = (255, 50, 255)

    # Queue to store locations of index and pinky finger tips for the last 150 frames
    index_finger_tip_locations = deque(maxlen=50)
    pinky_finger_tip_locations = deque(maxlen=30)
    
    hold_z = 0
    hold_j = 0
    
    run_z = False
    run_j = False
    
    if letter == 'z':
        run_z = True
    elif letter == 'j':
        run_j = True

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break
        
        text = ''
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        
        if run_z:
             # If hands are detected, draw landmarks on the frame and store index finger tip location
            if results.multi_hand_landmarks:
                for lms in results.multi_hand_landmarks:
                    # Draw hand landmarks
                    mp_drawing.draw_landmarks(frame, lms, mp_hand.HAND_CONNECTIONS)
                    
                    if not (is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)) and
                        is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)) and
                        is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
                        is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms))):
                        
                        if not hold_z:
                            index_finger_tip_locations.append((None, None))
                        continue
                    
                    # Get index finger tip location
                    image_height, image_width, _ = frame.shape
                    index_finger_tip_x = int(index_tip(lms).x * image_width)
                    index_finger_tip_y = int(index_tip(lms).y * image_height)

                    # Store index tip location
                    if not hold_z:
                        index_finger_tip_locations.append((index_finger_tip_x, index_finger_tip_y))
            else:
                if not hold_z:
                    index_finger_tip_locations.append((None, None))
                
            # Draw index finger tip locations from the last 50 frames
            for x, y in index_finger_tip_locations:
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
                
            z_found, corners = detect_z(index_finger_tip_locations)
            
            if z_found or hold_z > 0:
                text = 'Z'
                hold_z += 1
            
            if hold_z == 50:
                hold_z = 0
                index_finger_tip_locations.clear()
                
            for corner in corners:
                cv2.circle(frame, (int(corner[0]), int(corner[1])), 7, (0, 0, 255), -1)
                
        elif run_j:
            # If hands are detected, draw landmarks on the frame and store pinky finger tip location
            if results.multi_hand_landmarks:
                for lms in results.multi_hand_landmarks:
                    # Draw hand landmarks
                    mp_drawing.draw_landmarks(frame, lms, mp_hand.HAND_CONNECTIONS)
                    
                    # Get index finger tip location
                    # Using finger_mcp instead of wrist because of the way the hand moves when signing 'j'
                    if not (
                        # is_finger_closed_slope(index_tip(lms), index_pip(lms), index_mcp(lms)) and
                        # is_finger_closed_slope(middle_tip(lms), middle_pip(lms), middle_mcp(lms)) and
                        # is_finger_closed_slope(ring_tip(lms), ring_pip(lms), ring_mcp(lms)) and
                        is_finger_open_slope(pinky_tip(lms), pinky_pip(lms), pinky_mcp(lms))):
                        
                        pinky_finger_tip_locations.append((None, None))
                        continue

                    # Get pinky finger tip location
                    pinky_finger_tip = lms.landmark[mp_hand.HandLandmark.PINKY_TIP]
                    image_height, image_width, _ = frame.shape
                    pinky_finger_tip_x = int(pinky_finger_tip.x * image_width)
                    pinky_finger_tip_y = int(pinky_finger_tip.y * image_height)

                    # Store pinky finger tip location
                    pinky_finger_tip_locations.append((pinky_finger_tip_x, pinky_finger_tip_y))
            else:
                pinky_finger_tip_locations.append((None, None))
                
            # Draw pinky finger tip locations from the last 50 frames
            for x, y in pinky_finger_tip_locations:
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            
            j_found, xc, yc, R = detect_j(pinky_finger_tip_locations)
         
            if j_found or hold_j > 0:
                text = 'J'
                hold_j += 1
                
            if hold_j == 50:
                hold_j = 0
            if False: #R > 0: # Uncomment to show the circle being fit to the points
                cv2.circle(frame, (int(xc), int(yc)), int(R), (200, 0, 0), thickness=2)
                
        cv2.putText(frame, text, text_position_left, font, font_scale, color, font_thickness)
        cv2.imshow("Hand Tracking", frame)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Hand Tracking', cv2.WND_PROP_VISIBLE) < 1:
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
        
    run_motion_module(args.letter.lower())