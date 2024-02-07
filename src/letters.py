import mediapipe as mp
from helpers import *
from hand_landmarks import *

# Letter 'A'
# The letter a is defined by the two following propertes:
# - The hand(four fingers) is closed
# - the thumb is to the side of all of the fingers (not across any fingers)
# returns: true if all the above proprties are true, false otherwise
def is_letter_a(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    index_mcp = index_mcp_lm(landmarks)
    index_dip = index_dip_lm(landmarks)
    
    # Right Hand
    if handedness:
        return is_hand_closed(landmarks) and thumb_tip.y < thumb_mcp.y and thumb_tip.x > max(index_mcp.x, index_dip.x)
    # Left Hand
    else:
        return is_hand_closed(landmarks) and thumb_tip.y < thumb_mcp.y and thumb_tip.x < min(index_mcp.x, index_dip.x)
        
def is_letter_b(results, landmarks):
    return False

def is_letter_c(results, landmarks):
    return False

def is_letter_d(_, landmarks):
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    return (not is_finger_open(middle_tip, middle_pip, wrist) and
           not is_finger_open(ring_tip, ring_pip, wrist) and
           not is_finger_open(pinky_tip, pinky_pip, wrist) and
           is_finger_open(index_tip, index_pip, wrist) and
           is_touching(thumb_tip, middle_tip, middle_dip))
    

def is_letter_e(results, landmarks):
    return False

def is_letter_f(results, landmarks):
    return False

def is_letter_g(results, landmarks):
    return False

def is_letter_h(results, landmarks):
    return False

def is_letter_i(results, landmarks):
    return False

def is_letter_j(results, landmarks):
    return False

def is_letter_k(results, landmarks):
    return False

def is_letter_l(results, landmarks):
    return False

def is_letter_m(results, landmarks):
    return False

def is_letter_n(results, landmarks):
    return False

def is_letter_o(results, landmarks):
    return False

def is_letter_p(results, landmarks):
    return False

def is_letter_q(results, landmarks):
    return False

def is_letter_r(results, landmarks):
    return False

def is_letter_s(results, landmarks):
    return False

def is_letter_t(results, landmarks):
    return False

def is_letter_u(results, landmarks):
    return False

def is_letter_v(results, landmarks):
    return False

def is_letter_w(results, landmarks):
    return False

def is_letter_x(results, landmarks):
    return False

def is_letter_y(results, landmarks):
    return False

def is_letter_z(results, landmarks):
    return False
