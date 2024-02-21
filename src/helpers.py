import mediapipe as mp
import numpy as np
from hand_landmarks import *
import math

def is_hand_open(landmarks):
    # Define the indices for the thumb and index finger landmarks
    wrist = wrist_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    # Check if each induvidual finger is open
    index_open = is_finger_open(index_tip, index_pip, wrist)
    middle_open = is_finger_open(middle_tip, middle_pip, wrist)
    ring_open = is_finger_open(ring_tip, ring_pip, wrist)
    pinky_open = is_finger_open(pinky_tip, pinky_pip, wrist)

    return index_open and middle_open and ring_open and pinky_open

def is_hand_closed(landmarks):
    # Define the indices for the thumb and index finger landmarks
    wrist = wrist_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    # Check if each induvidual finger is closed
    index_closed = not is_finger_open(index_tip, index_pip, wrist)
    middle_closed = not is_finger_open(middle_tip, middle_pip, wrist)
    ring_closed = not is_finger_open(ring_tip, ring_pip, wrist)
    pinky_closed = not is_finger_open(pinky_tip, pinky_pip, wrist)

    return index_closed and middle_closed and ring_closed and pinky_closed

def is_finger_open(finger_tip, finger_pip, wrist):
    if wrist.y < finger_pip.y:
        return finger_tip.y > finger_pip.y
    else:
        return finger_tip.y < finger_pip.y
    

def is_right_hand(results, landmarks):
    return results.multi_handedness[
                results.multi_hand_landmarks.index(landmarks)
            ].classification[0].label == 'Left'
    
def distance(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

def normalized_slope(a, b):
    '''
    Gives a normalized slope from 0 - 1, 0 being horizontal and 1 being vertical.
    '''
    if a.x == b.x:
       return 1
    slope_value = (a.y - b.y) / (a.x - b.x)
    return math.atan(slope_value) / (math.pi / 2)

def is_touching(finger1_tip, finger2_tip, finger2_dip):
    return distance(finger1_tip, finger2_tip) * 1.25 < distance(finger2_tip, finger2_dip)

def is_facing_forward(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    
    thumb_cmc = thumb_cmc_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    index_mcp = index_mcp_lm(landmarks)
    middle_mcp = middle_mcp_lm(landmarks)
    ring_mcp = ring_mcp_lm(landmarks)
    pinky_mcp = pinky_mcp_lm(landmarks)
    
    if handedness:
        return pinky_mcp.x < ring_mcp.x < middle_mcp.x < index_mcp.x and thumb_cmc.y > thumb_mcp.y
    else:
        return pinky_mcp.x > ring_mcp.x > middle_mcp.x > index_mcp.x  and thumb_cmc.y > thumb_mcp.y
    