import mediapipe as mp
from helpers.helpers import *
from helpers.hand_landmarks import *

# Letter 'A'
# The letter a is defined by the two following propertes:
# - The hand(four fingers) is closed
# - the thumb is to the side of all of the fingers (not across any fingers)
# returns: true if all the above proprties are true, false otherwise
def is_letter_a(results, lms):
    handedness = is_right_hand(results, lms)
    
    # Right Hand
    if handedness:
        return (is_facing_forward(results, lms) and
                is_hand_closed(lms) and
                thumb_tip(lms).x > max(index_mcp(lms).x, index_dip(lms).x) and 
                index_tip(lms).y > middle_pip(lms).y and
                is_touching_horizontal(index_mcp(lms), thumb_tip(lms), thumb_ip(lms)))
    # Left Hand
    else:
        return (is_facing_forward(results, lms) and
                is_hand_closed(lms) and
                thumb_tip(lms).x < min(index_mcp(lms).x, index_dip(lms).x) and 
                index_tip(lms).y > middle_pip(lms).y and
                is_touching_horizontal(thumb_tip(lms), index_mcp(lms), index_pip(lms)))
        
def is_letter_b(results, lms):
    handedness = is_right_hand(results, lms)
    
    if handedness:
        return (is_facing_forward(results, lms) and 
                is_hand_open(lms) and
                is_touching(index_dip(lms), middle_dip(lms), middle_pip(lms)) and
                is_touching(middle_dip(lms), ring_dip(lms), ring_pip(lms)) and
                is_touching(ring_dip(lms), pinky_tip(lms), pinky_dip(lms)) and
                thumb_ip(lms).x - thumb_tip(lms).x > abs(thumb_tip(lms).y - thumb_ip(lms).y))
    else:
        return (is_facing_forward(results, lms) and
                is_hand_open(lms) and
                is_touching(index_dip(lms), middle_dip(lms), middle_pip(lms)) and
                is_touching(middle_dip(lms), ring_dip(lms), ring_pip(lms)) and
                is_touching(ring_dip(lms), pinky_tip(lms), pinky_dip(lms)) and
                thumb_tip(lms).x - thumb_ip(lms).x > abs(thumb_tip(lms).y - thumb_ip(lms).y))

                

def is_letter_c(results, lms):
    
    return (not is_facing_forward(results, lms) and
            not is_facing_back_and_sideways(results, lms) and
            distance(index_mcp(lms), pinky_mcp(lms)) < 0.7 * distance(index_mcp(lms), wrist(lms)) and
            wrist(lms).y > index_mcp(lms).y and
            is_hand_closed_sideways(results, lms) and  
            not is_touching(index_tip(lms), thumb_tip(lms), thumb_ip(lms)) and
            not is_touching(middle_tip(lms), thumb_tip(lms), thumb_ip(lms)) and
            not is_touching(ring_tip(lms), thumb_tip(lms), thumb_ip(lms)) and
            not is_touching(pinky_tip(lms), thumb_tip(lms), thumb_ip(lms)))

def is_letter_d(results, lms):

    return (is_facing_forward(results, lms) and
            is_touching(thumb_tip(lms), middle_tip(lms), middle_dip(lms)) and
            is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)) and
            is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)) and
            is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)))
    

def is_letter_e(results, lms):
    handedness = is_right_hand(results, lms)
    thumb_slope = normalized_slope(thumb_tip(lms), thumb_ip(lms))
    
    if handedness:
        return (is_facing_forward(results, lms) and
            is_hand_closed(lms) and
            thumb_tip(lms).y > max(index_tip(lms).y, middle_tip(lms).y, ring_tip(lms).y, pinky_tip(lms).y) and
            thumb_slope > -0.4 and
            thumb_slope < 0.4 and 
            thumb_tip(lms).x < thumb_ip(lms).x)
    else:
        return (is_facing_forward(results, lms) and
            is_hand_closed(lms) and
            thumb_tip(lms).y > max(index_tip(lms).y, middle_tip(lms).y, ring_tip(lms).y, pinky_tip(lms).y) and
            thumb_slope > -0.4 and
            thumb_slope < 0.4 and
            thumb_tip(lms).x > thumb_ip(lms).x)

def is_letter_f(results, lms):

    return (is_facing_forward(results, lms) and
           is_touching(index_tip(lms), thumb_tip(lms), thumb_ip(lms)) and #Uses thumb tip and ip to provide more tollerance
           is_finger_closed(index_tip(lms), index_pip(lms), wrist(lms)) and
           is_finger_open(middle_tip(lms), middle_dip(lms), wrist(lms)) and
           is_finger_open(ring_tip(lms), ring_dip(lms), wrist(lms)) and
           is_finger_open(pinky_tip(lms), pinky_dip(lms), wrist(lms)))
 

def is_letter_g(results, lms):
    handedness = is_right_hand(results, lms)
    
    return (is_hand_closed_sideways(results, lms) and
            wrist(lms).y > index_mcp(lms).y and
            thumb_tip(lms).y > index_pip(lms).y and 
            is_finger_open_sideways(thumb_tip(lms), thumb_ip(lms), handedness) and
            is_finger_open_sideways(index_tip(lms), index_pip(lms), handedness) and
            is_finger_closed_sideways(middle_tip(lms), middle_dip(lms), handedness) and 
            is_finger_closed_sideways(ring_tip(lms), ring_dip(lms), handedness) and
            is_finger_closed_sideways(pinky_tip(lms), pinky_dip(lms), handedness)) 

def is_letter_h(results, lms):
    handedness = is_right_hand(results, lms)
    
    return (is_hand_closed_sideways(results, lms) and
            wrist(lms).y > index_mcp(lms).y and
            thumb_tip(lms).y > index_pip(lms).y and 
            is_finger_open_sideways(index_tip(lms), index_pip(lms), handedness) and
            is_finger_open_sideways(middle_tip(lms), middle_pip(lms), handedness) and 
            is_finger_closed_sideways(ring_tip(lms), ring_dip(lms), handedness) and
            is_finger_closed_sideways(pinky_tip(lms), pinky_dip(lms), handedness)and 
            is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms))) 

def is_letter_i(results, lms):
    handedness = is_right_hand(results, lms)
    
    if handedness: # Right hand
        return (is_facing_forward(results, lms) and
                thumb_tip(lms).x > max(index_mcp(lms).x, index_dip(lms).x) and
                is_touching(index_mcp(lms), thumb_tip(lms), thumb_ip(lms)) and
                is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)) and
                is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
                is_finger_open(pinky_tip(lms), pinky_dip(lms), wrist(lms)) and
                is_finger_closed(index_tip(lms), index_pip(lms), wrist(lms))
)
    else: # Left hand
        return (is_facing_forward(results, lms) and
                thumb_tip(lms).x < min(index_mcp(lms).x, index_dip(lms).x) and
                not (normalized_slope(thumb_mcp(lms), thumb_tip(lms)) < .8 and
                normalized_slope(thumb_mcp(lms), thumb_tip(lms)) > 0) and
                is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)) and
                is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
                is_finger_open(pinky_tip(lms), pinky_dip(lms), wrist(lms)) and
                is_finger_closed(index_tip(lms), index_pip(lms), wrist(lms))
)


def is_letter_j(results, lms):
    return False

def is_letter_k(results, lms):
    return (is_facing_forward(results, lms) and
            thumb_tip(lms).x > min(index_pip(lms).x, middle_pip(lms).x) and
            thumb_tip(lms).x < max(index_pip(lms).x, middle_pip(lms).x) and
            thumb_tip(lms).y < index_mcp(lms).y and
            is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)) and
            is_finger_open(middle_tip(lms), middle_dip(lms), wrist(lms)) and
            is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)) and 
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)))
            

def is_letter_l(results, lms):
    
    return (is_facing_forward(results, lms) and
            abs(normalized_slope(index_mcp(lms), index_tip(lms))) - abs(normalized_slope(thumb_mcp(lms), thumb_tip(lms))) > 0.5 and
           is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)) and
           is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
           is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)) and
           is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)))

def is_letter_m(results, lms):
    
    return (is_facing_forward(results, lms) and
            is_hand_closed(lms) and
            is_touching(thumb_tip(lms),pinky_pip(lms), pinky_dip(lms)) and
            is_touching(thumb_tip(lms), ring_pip(lms), ring_dip(lms)) and
            ring_pip(lms).y < thumb_tip(lms).y < pinky_pip(lms).y)

def is_letter_n(results, lms):
    handedness = is_right_hand(results, lms)
    
    if handedness:
        return (is_facing_forward(results, lms) and
                is_hand_closed(lms) and
                is_touching(thumb_tip(lms), middle_pip(lms), middle_dip(lms)) and
                is_touching(thumb_tip(lms), ring_pip(lms), ring_dip(lms)) and
                middle_pip(lms).y < thumb_tip(lms).y < ring_pip(lms).y and
                thumb_tip(lms).x < middle_pip(lms).x)
    else:
        return (is_facing_forward(results, lms) and
                is_hand_closed(lms) and
                is_touching(thumb_tip(lms), middle_pip(lms), middle_dip(lms)) and
                is_touching(thumb_tip(lms), ring_pip(lms), ring_dip(lms)) and
                middle_pip(lms).y < thumb_tip(lms).y < ring_pip(lms).y and
                thumb_tip(lms).x > middle_pip(lms).x)
    
def is_letter_o(results, lms):
    
    return (not is_facing_forward(results, lms) and
            wrist(lms).y > index_mcp(lms).y and
            not is_facing_back_and_sideways(results, lms) and
            is_hand_closed_sideways(results, lms) and
            (is_touching(index_tip(lms), thumb_tip(lms), thumb_ip(lms)) or
             is_touching(middle_tip(lms), thumb_tip(lms), thumb_ip(lms)) or
             is_touching(ring_tip(lms), thumb_tip(lms), thumb_ip(lms)) or
             is_touching(pinky_tip(lms), thumb_tip(lms), thumb_ip(lms))))

def is_letter_p(results, lms):
    
    return (is_facing_back_upside_down(results, lms) and
            min(index_pip(lms).x, middle_pip(lms).x) < thumb_tip(lms).x < max(index_pip(lms).x, middle_pip(lms).x) and
            is_finger_open(index_tip(lms), index_pip(lms), wrist(lms)) and
            is_finger_open(middle_tip(lms), middle_pip(lms), wrist(lms)) and
            is_finger_closed(ring_tip(lms), ring_dip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_dip(lms), wrist(lms)) and
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)))
    

def is_letter_q(results, lms):
    handedness = is_right_hand(results, lms)
    
    return (is_facing_back_upside_down(results, lms) and
            is_finger_open(index_tip(lms), index_pip(lms), wrist(lms)) and
            is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)) and
            is_finger_closed(ring_tip(lms), ring_dip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_dip(lms), wrist(lms)) and
            not is_touching_close(thumb_tip(lms), index_tip(lms), index_dip(lms)) and
            ((handedness and thumb_tip(lms).x < index_tip(lms).x) or
            (not handedness and thumb_tip(lms).x > index_tip(lms).x)))

def is_letter_r(results, lms):
    handedness = is_right_hand(results, lms)

    if handedness: # Right hand
        return (is_facing_forward(results, lms) and
            is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)) and
            (is_touching(thumb_tip(lms), ring_dip(lms), ring_tip(lms)) or
            is_touching(thumb_tip(lms), ring_tip(lms), ring_dip(lms))) and
            is_finger_open(middle_tip(lms), middle_dip(lms), wrist(lms)) and
            is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)) and 
            is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)) and
            index_tip(lms).x < middle_tip(lms).x)
    else: # Left hand
        return (is_facing_forward(results, lms) and
            is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)) and
            is_finger_open(middle_tip(lms), middle_dip(lms), wrist(lms)) and
            is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)) and 
            is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)) and
            index_tip(lms).x > middle_tip(lms).x)

def is_letter_s(results, lms):
    
    left = min(index_tip(lms).x, index_pip(lms).x, pinky_tip(lms).x, pinky_pip(lms).x)
    right = max(index_tip(lms).x, index_pip(lms).x, pinky_tip(lms).x, pinky_pip(lms).x)
    top = min(index_tip(lms).y, index_pip(lms).y, pinky_tip(lms).y, pinky_pip(lms).y)
    bottom = max(index_tip(lms).y, index_pip(lms).y, pinky_tip(lms).y, pinky_pip(lms).y)
    
    return (is_facing_forward(results, lms) and
            is_hand_closed(lms) and
            left < thumb_tip(lms).x < right and
            top < thumb_tip(lms).y < bottom)

def is_letter_t(results, lms):
       
    return (is_facing_forward(results, lms) and
            is_hand_closed(lms) and
            thumb_tip(lms).x < max(index_pip(lms).x, middle_pip(lms).x) and
            thumb_tip(lms).x > min(index_pip(lms).x, middle_pip(lms).x))

def is_letter_u(results, lms):
    handedness = is_right_hand(results, lms)
    
    return (is_facing_forward(results, lms) and
            is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)) and
            is_finger_open(middle_tip(lms), middle_dip(lms), wrist(lms)) and
            is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)) and 
            is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)) and
            ((handedness and index_tip(lms).x > middle_tip(lms).x) or 
             (not handedness and index_tip(lms).x < middle_tip(lms).x)) and
            (is_touching_close(thumb_tip(lms), ring_dip(lms), ring_tip(lms)) or
            is_touching_close(thumb_tip(lms), ring_tip(lms), ring_dip(lms))))

def is_letter_v(results, lms):
    
    return (is_facing_forward(results, lms) and
            is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)) and
            is_finger_open(middle_tip(lms), middle_dip(lms), wrist(lms)) and
            is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)) and 
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)) and
            (is_touching_close(thumb_tip(lms), ring_dip(lms), ring_tip(lms)) or
            is_touching_close(thumb_tip(lms), ring_tip(lms), ring_dip(lms))))

def is_letter_w(results, lms):
    
    return (is_facing_forward(results, lms) and
            is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)) and
            is_finger_open(middle_tip(lms), middle_dip(lms), wrist(lms)) and
            is_finger_open(ring_tip(lms), ring_dip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)) and 
            not is_touching(ring_tip(lms), middle_tip(lms), middle_dip(lms)) and
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)) and
            is_touching(pinky_tip(lms), thumb_tip(lms), thumb_mcp(lms)))

def is_letter_x(_, lms):
    
    return (abs(normalized_slope(wrist(lms), middle_mcp(lms))) > 0.7 and
            is_index_x(index_tip(lms), index_pip(lms), index_mcp(lms)) and
            is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)) and 
            is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
            is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)) and
            (is_touching(thumb_tip(lms), middle_pip(lms), middle_dip(lms)) or
             is_touching(thumb_tip(lms), middle_dip(lms), middle_pip(lms))))

def is_letter_y(results, lms):
    handedness = is_right_hand(results, lms)

    if handedness: # Right hand
        return (is_facing_forward(results, lms) and
                thumb_tip(lms).x > max(index_mcp(lms).x, index_dip(lms).x) and
                not is_touching_far(index_mcp(lms), thumb_tip(lms), thumb_ip(lms)) and
                is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)) and
                is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
                is_finger_open(pinky_tip(lms), pinky_dip(lms), wrist(lms)) and
                is_finger_closed(index_tip(lms), index_pip(lms), wrist(lms))
)
    else: # Left hand
        return (is_facing_forward(results, lms) and
                thumb_tip(lms).x < min(index_mcp(lms).x, index_dip(lms).x) and 
                not is_touching_far(index_mcp(lms), thumb_tip(lms), thumb_ip(lms)) and
                is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)) and
                is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)) and
                is_finger_open(pinky_tip(lms), pinky_dip(lms), wrist(lms)) and
                is_finger_closed(index_tip(lms), index_pip(lms), wrist(lms))
)

def is_letter_z(results, lms):
    return False

letter_functions = {
    'a': is_letter_a,
    'b': is_letter_b,
    'c': is_letter_c,
    'd': is_letter_d,
    'e': is_letter_e,
    'f': is_letter_f,
    'g': is_letter_g,
    'h': is_letter_h,
    'i': is_letter_i,
    'j': is_letter_j,
    'k': is_letter_k,
    'l': is_letter_l,
    'm': is_letter_m,
    'n': is_letter_n,
    'o': is_letter_o,
    'p': is_letter_p,
    'q': is_letter_q,
    'r': is_letter_r,
    's': is_letter_s,
    't': is_letter_t,
    'u': is_letter_u,
    'v': is_letter_v,
    'w': is_letter_w,
    'x': is_letter_x,
    'y': is_letter_y,
    'z': is_letter_z
}