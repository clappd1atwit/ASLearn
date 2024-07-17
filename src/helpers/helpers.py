import mediapipe as mp
import numpy as np
from helpers.hand_landmarks import *
import math
import config.config as cfg

def is_hand_open(lms):

    # Check if each induvidual finger is open
    index_open = is_finger_open(index_tip(lms), index_dip(lms), wrist(lms))
    middle_open = is_finger_open(middle_tip(lms), middle_dip(lms), wrist(lms))
    ring_open = is_finger_open(ring_tip(lms), ring_dip(lms), wrist(lms))
    pinky_open = is_finger_open(pinky_tip(lms), pinky_dip(lms), wrist(lms))

    return index_open and middle_open and ring_open and pinky_open

def is_hand_closed(lms):

    # Check if each induvidual finger is closed
    return (is_finger_closed(index_tip(lms), index_pip(lms), wrist(lms)) and
            is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)) and
            is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)))

def is_hand_closed_sideways(results, lms):
    
    handedness = is_right_hand(results, lms)

    # Check if each induvidual finger is closed
    if handedness:
        return (normalized_slope(index_tip(lms), index_pip(lms)) > -0.5 and
                normalized_slope(middle_tip(lms), middle_pip(lms)) > -0.4 and
                normalized_slope(ring_tip(lms), ring_pip(lms)) > -0.3 and
                normalized_slope(pinky_tip(lms), pinky_pip(lms)) > -0.3)
    else:
        return (normalized_slope(index_tip(lms), index_pip(lms)) < 0.5 and
                normalized_slope(middle_tip(lms), middle_pip(lms)) < 0.4 and
                normalized_slope(ring_tip(lms), ring_pip(lms)) < 0.3 and
                normalized_slope(pinky_tip(lms), pinky_pip(lms)) < 0.3)

def is_finger_open(finger_tip, finger_dip, wrist):
    if wrist.y > finger_dip.y:
        return finger_tip.y < finger_dip.y
    else:
        return finger_tip.y > finger_dip.y
    
def is_finger_open_slope(finger_tip, finger_pip, finger_mcp):
    vector_tip_pip = (finger_tip.x - finger_pip.x, finger_tip.y - finger_pip.y)
    vector_mcp_pip = (finger_mcp.x - finger_pip.x, finger_mcp.y - finger_pip.y)
    
    dot_product = (vector_tip_pip[0] * vector_mcp_pip[0]) + (vector_tip_pip[1] * vector_mcp_pip[1])
    
    # Calculate the magnitudes of the vectors
    magnitude_tip_pip = math.sqrt(vector_tip_pip[0]**2 + vector_tip_pip[1]**2)
    magnitude_mcp_pip = math.sqrt(vector_mcp_pip[0]**2 + vector_mcp_pip[1]**2)
    
    # Calculate the cosine of the angle between the vectors
    cos_angle = dot_product / (magnitude_tip_pip * magnitude_mcp_pip)
    angle = math.degrees(math.acos(cos_angle))
    
    return angle > 120
    
def is_finger_closed(finger_tip, finger_pip, wrist):
    if wrist.y > finger_pip.y:
        return finger_tip.y > finger_pip.y
    else:
        return finger_tip.y < finger_pip.y
    
def is_finger_closed_slope(finger_tip, finger_pip, finger_mcp):
    vector_tip_pip = (finger_tip.x - finger_pip.x, finger_tip.y - finger_pip.y)
    vector_mcp_pip = (finger_mcp.x - finger_pip.x, finger_mcp.y - finger_pip.y)
    
    dot_product = (vector_tip_pip[0] * vector_mcp_pip[0]) + (vector_tip_pip[1] * vector_mcp_pip[1])
    
    # Calculate the magnitudes of the vectors
    magnitude_tip_pip = math.sqrt(vector_tip_pip[0]**2 + vector_tip_pip[1]**2)
    magnitude_mcp_pip = math.sqrt(vector_mcp_pip[0]**2 + vector_mcp_pip[1]**2)
    
    # Calculate the cosine of the angle between the vectors
    cos_angle = dot_product / (magnitude_tip_pip * magnitude_mcp_pip)
    angle = math.degrees(math.acos(cos_angle))
    
    return angle < 100

def is_right_hand(results, lms):
    return results.multi_handedness[
                results.multi_hand_landmarks.index(lms)
            ].classification[0].label == cfg.handedness_calibration
    
def distance(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

def normalized_slope(a, b):
    '''
    Gives a normalized slope from 0 - 1, 0 being horizontal and 1 being vertical.
    A negative slope is given for negative slopes which can be used to distiguish
    between left and right hand positions
    '''
    if a.x == b.x:
       return 1
    slope_value = (a.y - b.y) / (a.x - b.x)
    return math.atan(slope_value) / (math.pi / 2)

def is_touching(finger1_tip, finger2_tip, finger2_dip):
    return distance(finger1_tip, finger2_tip) < distance(finger2_tip, finger2_dip) * 1.25

def is_touching_close(finger1_tip, finger2_tip, finger2_dip):
    return distance(finger1_tip, finger2_tip) < distance(finger2_tip, finger2_dip)

def is_touching_far(finger1_tip, finger2_tip, finger2_dip):
    return distance(finger1_tip, finger2_tip) < distance(finger2_tip, finger2_dip) * 1.5

def is_touching_horizontal(finger1_tip, finger2_tip, finger2_dip):
    return abs(finger1_tip.x - finger2_tip.x) < distance(finger2_tip, finger2_dip) * 1.25

def is_facing_forward(results, lms):
    handedness = is_right_hand(results, lms)
    
    if handedness:
        return (pinky_mcp(lms).x < ring_mcp(lms).x < middle_mcp(lms).x < index_mcp(lms).x and 
                thumb_cmc(lms).y > thumb_mcp(lms).y and
                distance(index_mcp(lms), pinky_mcp(lms)) > distance(index_mcp(lms), wrist(lms)) / 3)
    else:
        return (pinky_mcp(lms).x > ring_mcp(lms).x > middle_mcp(lms).x > index_mcp(lms).x  and 
                thumb_cmc(lms).y > thumb_mcp(lms).y and
                distance(index_mcp(lms), pinky_mcp(lms)) > distance(index_mcp(lms), wrist(lms)) / 3)
        
def is_facing_back_upside_down(results, lms):
    handedness = is_right_hand(results, lms)
    
    if handedness:
        return (pinky_mcp(lms).x < index_mcp(lms).x and
                pinky_mcp(lms).y > wrist(lms).y and
                distance(index_mcp(lms), pinky_mcp(lms)) > distance(index_mcp(lms), wrist(lms)) / 3)
    else:
        return (pinky_mcp(lms).x > index_mcp(lms).x and
                pinky_mcp(lms).y > wrist(lms).y and
                distance(index_mcp(lms), pinky_mcp(lms)) > distance(index_mcp(lms), wrist(lms)) / 3)
        
def is_facing_back_and_sideways(results, lms):
    handedness = is_right_hand(results, lms)
    
    if handedness:
        return (pinky_mcp(lms).y > ring_mcp(lms).y > middle_mcp(lms).y > index_mcp(lms).y and
                abs(normalized_slope(pinky_mcp(lms), index_mcp(lms))) > 0.4 and
                index_mcp(lms).x > wrist(lms).x)
    else:
        return (pinky_mcp(lms).y > ring_mcp(lms).y > middle_mcp(lms).y > index_mcp(lms).y and
                abs(normalized_slope(pinky_mcp(lms), index_mcp(lms))) > 0.4 and
                index_mcp(lms).x < wrist(lms).x)
    
def is_finger_open_sideways(finger_tip, finger_dip, handedness):
    if handedness:
        return finger_tip.x > finger_dip.x
    else:
        return finger_tip.x < finger_dip.x
    
def is_finger_closed_sideways(finger_tip, finger_pip, handedness):
    if handedness:
        return finger_tip.x < finger_pip.x
    else:
        return finger_tip.x > finger_pip.x
    
def is_index_x(index_tip, index_pip, index_mcp):
    return (normalized_slope(index_tip, index_pip) < .5 and
            normalized_slope(index_tip, index_pip) > -.5 and
            (normalized_slope(index_mcp, index_pip) > 0.7 or
            normalized_slope(index_mcp, index_pip) < -0.7))