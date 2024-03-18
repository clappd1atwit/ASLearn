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
    
    print(normalized_slope(thumb_mcp, thumb_tip))
            
    # Right Hand
    if handedness:
        return (is_facing_forward(results, landmarks) and
                is_hand_closed(landmarks) and
                thumb_tip.x > max(index_mcp.x, index_dip.x) and 
                (normalized_slope(thumb_mcp, thumb_tip) > .7 or
                normalized_slope(thumb_mcp, thumb_tip) < -.7))
    # Left Hand
    else:
        return (is_facing_forward(results, landmarks) and
                is_hand_closed(landmarks) and
                thumb_tip.x < min(index_mcp.x, index_dip.x) and 
                (normalized_slope(thumb_mcp, thumb_tip) > .7 or
                normalized_slope(thumb_mcp, thumb_tip) < -.7))
        
def is_letter_b(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_ip = thumb_ip_lm(landmarks)
    
    if handedness:
        return (is_facing_forward(results, landmarks) and 
                is_hand_open(landmarks) 
                and thumb_ip.x - thumb_tip.x > abs(thumb_tip.y - thumb_ip.y))
    else:
        return (is_facing_forward(results, landmarks) and
                is_hand_open(landmarks) 
                and thumb_tip.x - thumb_ip.x > abs(thumb_tip.y - thumb_ip.y))

                

def is_letter_c(results, landmarks):
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_ip = thumb_ip_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    return (not is_facing_forward(results, landmarks) and
            is_hand_closed_sideways(results, landmarks) and  
            not is_touching(index_tip, thumb_tip, thumb_ip) and
            not is_touching(middle_tip, thumb_tip, thumb_ip) and
            not is_touching(ring_tip, thumb_tip, thumb_ip) and
            not is_touching(pinky_tip, thumb_tip, thumb_ip))

def is_letter_d(results, landmarks):
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

    return (is_facing_forward(results, landmarks) and
           not is_finger_open(middle_tip, middle_pip, wrist) and
           not is_finger_open(ring_tip, ring_pip, wrist) and
           not is_finger_open(pinky_tip, pinky_pip, wrist) and
           is_finger_open(index_tip, index_pip, wrist) and
           is_touching(thumb_tip, middle_tip, middle_dip))
    

def is_letter_e(results, landmarks):
    handedness = is_right_hand(results, landmarks)

    thumb_ip = thumb_ip_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    
    index_tip = index_tip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_slope = normalized_slope(thumb_tip, thumb_ip)
    
    if handedness:
        return (is_facing_forward(results, landmarks) and
            is_hand_closed(landmarks) and
            thumb_tip.y > index_tip.y and
            thumb_tip.y > middle_tip.y and
            thumb_tip.y > ring_tip.y and
            thumb_tip.y > pinky_tip.y and
            thumb_slope > -0.2 and
            thumb_slope < 0.2 and 
            thumb_tip.x < thumb_ip.x)
    else:
        return (is_facing_forward(results, landmarks) and
            is_hand_closed(landmarks) and
            thumb_tip.y > index_tip.y and
            thumb_tip.y > middle_tip.y and
            thumb_tip.y > ring_tip.y and
            thumb_tip.y > pinky_tip.y and
            thumb_slope > -0.2 and
            thumb_slope < 0.2 and
            thumb_tip.x > thumb_ip.x)

def is_letter_f(results, landmarks):
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_ip = thumb_ip_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    return (is_facing_forward(results, landmarks) and
           is_finger_open(middle_tip, middle_pip, wrist) and
           is_finger_open(ring_tip, ring_pip, wrist) and
           is_finger_open(pinky_tip, pinky_pip, wrist) and
           not is_finger_open(index_tip, index_pip, wrist) and
           is_touching(index_tip, thumb_tip, thumb_ip))
 

def is_letter_g(results, landmarks):
    return False

def is_letter_h(results, landmarks):
    return False

def is_letter_i(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    index_mcp = index_mcp_lm(landmarks)
    index_dip = index_dip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    if handedness: # Right hand
        return (is_facing_forward(results, landmarks) and
                thumb_tip.x > max(index_mcp.x, index_dip.x) and
                not (normalized_slope(thumb_mcp, thumb_tip) > -.8 and
                normalized_slope(thumb_mcp, thumb_tip) < 0) and
                not is_finger_open(middle_tip, middle_pip, wrist) and
                not is_finger_open(ring_tip, ring_pip, wrist) and
                is_finger_open(pinky_tip, pinky_pip, wrist) and
                not is_finger_open(index_tip, index_pip, wrist))
    else: # Left hand
        return (is_facing_forward(results, landmarks) and
                thumb_tip.x < min(index_mcp.x, index_dip.x) and
                not (normalized_slope(thumb_mcp, thumb_tip) < .8 and
                normalized_slope(thumb_mcp, thumb_tip) > 0) and
                not is_finger_open(middle_tip, middle_pip, wrist) and
                not is_finger_open(ring_tip, ring_pip, wrist) and
                is_finger_open(pinky_tip, pinky_pip, wrist) and
                not is_finger_open(index_tip, index_pip, wrist))


def is_letter_j(results, landmarks):
    return False

def is_letter_k(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_mcp = middle_mcp_lm(landmarks)
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            not is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            not is_touching(index_tip, middle_tip, middle_dip) and
            thumb_tip.x > min(index_mcp.x, middle_mcp.x) and
            thumb_tip.x < max(index_mcp.x, middle_mcp.x) and
            thumb_tip.y < index_mcp.y)
            

def is_letter_l(results, landmarks):
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    return (is_facing_forward(results, landmarks) and
           not is_finger_open(middle_tip, middle_pip, wrist) and
           not is_finger_open(ring_tip, ring_pip, wrist) and
           not is_finger_open(pinky_tip, pinky_pip, wrist) and
           is_finger_open(index_tip, index_pip, wrist) and
           normalized_slope(thumb_mcp,thumb_tip) < 0.3)

def is_letter_m(results, landmarks):
    return False

def is_letter_n(results, landmarks):
    return False

def is_letter_o(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_ip = thumb_ip_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    return (not is_facing_forward(results, landmarks) and
            is_hand_closed_sideways(results, landmarks) and
            (is_touching(index_tip, thumb_tip, thumb_ip) or
             is_touching(middle_tip, thumb_tip, thumb_ip) or
             is_touching(ring_tip, thumb_tip, thumb_ip) or
             is_touching(pinky_tip, thumb_tip, thumb_ip)))

def is_letter_p(results, landmarks):
    return False

def is_letter_q(results, landmarks):
    return False

def is_letter_r(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_mcp = middle_mcp_lm(landmarks)
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    if index_tip.x > middle_tip.x:
        return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            not is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            is_touching(index_tip, middle_tip, middle_dip) and
            thumb_tip.y > index_mcp.y)

def is_letter_s(results, landmarks):
    return False

def is_letter_t(results, landmarks):
    return False

def is_letter_u(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_mcp = middle_mcp_lm(landmarks)
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            not is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            is_touching(index_tip, middle_tip, middle_dip) and
            thumb_tip.y > index_mcp.y)

def is_letter_v(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_mcp = middle_mcp_lm(landmarks)
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            not is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            not is_touching(index_tip, middle_tip, middle_dip) and
            thumb_tip.y > index_mcp.y)

def is_letter_w(results, landmarks):
    wrist = wrist_lm(landmarks)
    
    index_mcp = index_mcp_lm(landmarks)
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    
    middle_mcp = middle_mcp_lm(landmarks)
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)
    
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_dip = thumb_mcp_lm(landmarks)
    return (is_facing_forward(results, landmarks) and
            is_finger_open(index_tip, index_pip, wrist) and
            is_finger_open(middle_tip, middle_pip, wrist) and
            is_finger_open(ring_tip, ring_pip, wrist) and
            not is_finger_open(pinky_tip, pinky_pip, wrist) and 
            not is_touching(ring_tip, middle_tip, middle_dip) and
            not is_touching(index_tip, middle_tip, middle_dip) and
            is_touching(pinky_tip, thumb_tip, thumb_dip) and
            thumb_tip.y > index_mcp.y)

def is_letter_x(results, landmarks):
    return False

def is_letter_y(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    wrist = wrist_lm(landmarks)
    thumb_tip = thumb_tip_lm(landmarks)
    thumb_mcp = thumb_mcp_lm(landmarks)
    
    index_pip = index_pip_lm(landmarks)
    index_tip = index_tip_lm(landmarks)
    index_mcp = index_mcp_lm(landmarks)
    index_dip = index_dip_lm(landmarks)
    
    middle_pip = middle_pip_lm(landmarks)
    middle_dip = middle_dip_lm(landmarks)
    middle_tip = middle_tip_lm(landmarks)
    
    ring_pip = ring_pip_lm(landmarks)
    ring_tip = ring_tip_lm(landmarks)
    
    pinky_pip = pinky_pip_lm(landmarks)
    pinky_tip = pinky_tip_lm(landmarks)

    if handedness: # Right hand
        return (is_facing_forward(results, landmarks) and
                (normalized_slope(thumb_mcp, thumb_tip) > -.7 and
                normalized_slope(thumb_mcp, thumb_tip) < 0) and
                not is_finger_open(middle_tip, middle_pip, wrist) and
                not is_finger_open(ring_tip, ring_pip, wrist) and
                is_finger_open(pinky_tip, pinky_pip, wrist) and
                not is_finger_open(index_tip, index_pip, wrist))
    else: # Left hand
        return (is_facing_forward(results, landmarks) and
                (normalized_slope(thumb_mcp, thumb_tip) < .7 and
                normalized_slope(thumb_mcp, thumb_tip) > 0) and
                not is_finger_open(middle_tip, middle_pip, wrist) and
                not is_finger_open(ring_tip, ring_pip, wrist) and
                is_finger_open(pinky_tip, pinky_pip, wrist) and
                not is_finger_open(index_tip, index_pip, wrist))

def is_letter_z(results, landmarks):
    return False

