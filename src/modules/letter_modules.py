from helpers import *
from letters import *
import hand_colors

idle_color = (255, 50, 255)
correct_color = (0, 200, 0)

def module_a(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_a(results, lms):
        text = 'A - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'A'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if ((handedness and thumb_tip(lms).x > max(index_mcp(lms).x, index_dip(lms).x) or
            not handedness and thumb_tip(lms).x < min(index_mcp(lms).x, index_dip(lms).x)) and 
            is_touching(index_mcp(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if is_finger_closed(index_tip(lms), index_pip(lms), wrist(lms)):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_b(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_b(results, lms):
        text = 'B - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'B'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if ((handedness and thumb_ip(lms).x - thumb_tip(lms).x > abs(thumb_tip(lms).y - thumb_ip(lms).y)) or 
            (not handedness and thumb_tip(lms).x - thumb_ip(lms).x > abs(thumb_tip(lms).y - thumb_ip(lms).y))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if (is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)) and
            is_touching(index_dip(lms), middle_dip(lms), middle_pip(lms))):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if (is_finger_open(middle_tip(lms), middle_dip(lms), wrist(lms)) and
            is_touching(middle_dip(lms), ring_dip(lms), ring_pip(lms))):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if (is_finger_open(ring_tip(lms), ring_dip(lms), wrist(lms)) and
            is_touching(ring_dip(lms), middle_dip(lms), middle_pip(lms))):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if (is_finger_open(pinky_tip(lms), pinky_dip(lms), wrist(lms)) and
            is_touching(ring_dip(lms), pinky_tip(lms), pinky_dip(lms))):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_c(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_c(results, lms):
        text = 'C - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'C'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if (not is_facing_forward(results, lms) and
            not is_facing_back_and_sideways(results, lms) and
            distance(index_mcp(lms), pinky_mcp(lms)) < 0.7 * distance(index_mcp(lms), wrist(lms)) and
            wrist(lms).y > index_mcp(lms).y):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if (not is_touching(index_tip(lms), thumb_tip(lms), thumb_ip(lms)) and
            not is_touching(middle_tip(lms), thumb_tip(lms), thumb_ip(lms)) and
            not is_touching(ring_tip(lms), thumb_tip(lms), thumb_ip(lms)) and
            not is_touching(pinky_tip(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if (((handedness and normalized_slope(index_tip(lms), index_pip(lms)) > -0.5) or
            (not handedness and normalized_slope(index_tip(lms), index_pip(lms)) < 0.5)) and 
            not is_touching(index_tip(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if (((handedness and normalized_slope(middle_tip(lms), middle_pip(lms)) > -0.4) or
            (not handedness and normalized_slope(middle_tip(lms), middle_pip(lms)) < 0.4)) and
            not is_touching(middle_tip(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if (((handedness and normalized_slope(ring_tip(lms), ring_pip(lms)) > -0.3) or
            (not handedness and normalized_slope(ring_tip(lms), ring_pip(lms)) < 0.3)) and
            not is_touching(ring_tip(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if (((handedness and normalized_slope(pinky_tip(lms), pinky_pip(lms)) > -0.3) or
            (not handedness and normalized_slope(pinky_tip(lms), pinky_pip(lms)) < 0.3)) and
            not is_touching(pinky_tip(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_d(results, lms):
    
    if is_letter_d(results, lms):
        text = 'D - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'D'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if is_touching(thumb_tip(lms), middle_tip(lms), middle_dip(lms)):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if is_finger_open(index_tip(lms), index_dip(lms), wrist(lms)):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_e(results, lms):
    handedness = is_right_hand(results, lms)
    thumb_slope = normalized_slope(thumb_tip(lms), thumb_ip(lms))
    
    if is_letter_e(results, lms):
        text = 'E - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'E'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if ((handedness and thumb_tip(lms).y > max(index_tip(lms).y, middle_tip(lms).y, ring_tip(lms).y, pinky_tip(lms).y) and
            thumb_slope > -0.4 and thumb_slope < 0.4 and thumb_tip(lms).x < thumb_ip(lms).x) or
            (not handedness and thumb_tip(lms).y > max(index_tip(lms).y, middle_tip(lms).y, ring_tip(lms).y, pinky_tip(lms).y) and
            thumb_slope > -0.4 and thumb_slope < 0.4 and thumb_tip(lms).x > thumb_ip(lms).x) and 
            is_touching(index_mcp(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if is_finger_closed(index_tip(lms), index_pip(lms), wrist(lms)):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_f(results, lms):
    if is_letter_f(results, lms):
        text = 'F - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'F'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if is_touching(index_tip(lms), thumb_tip(lms), thumb_ip(lms)):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if is_finger_closed(index_tip(lms), index_dip(lms), wrist(lms)):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if is_finger_open(middle_tip(lms), middle_pip(lms), wrist(lms)):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_open(ring_tip(lms), ring_pip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_open(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color


def module_g(results, lms):
    pass

def module_h(results, lms):
    pass

def module_i(results, lms):
    pass

def module_j(results, lms):
    pass

def module_k(results, lms):
    pass

def module_l(results, lms):
    pass

def module_m(results, lms):
    pass

def module_n(results, lms):
    pass

def module_o(results, lms):
    pass

def module_p(results, lms):
    pass

def module_q(results, lms):
    pass

def module_r(results, lms):
    pass

def module_s(results, lms):
    pass

def module_t(results, lms):
    pass

def module_u(results, lms):
    pass

def module_v(results, lms):
    pass

def module_w(results, lms):
    pass

def module_x(results, lms):
    pass

def module_y(results, lms):
    pass

def module_z(results, lms):
    pass

letter_modules = {
    'a': module_a,
    'b': module_b,
    'c': module_c,
    'd': module_d,
    'e': module_e,
    'f': module_f,
    'g': module_g,
    'h': module_h,
    'i': module_i,
    'j': module_j,
    'k': module_k,
    'l': module_l,
    'm': module_m,
    'n': module_n,
    'o': module_o,
    'p': module_p,
    'q': module_q,
    'r': module_r,
    's': module_s,
    't': module_t,
    'u': module_u,
    'v': module_v,
    'w': module_w,
    'x': module_x,
    'y': module_y,
    'z': module_z
}