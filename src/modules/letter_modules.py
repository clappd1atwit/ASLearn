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
    handedness = is_right_hand(results, lms)
    
    if is_letter_g(results, lms):
        text = 'G - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'G'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_hand_closed_sideways(results, lms) and wrist(lms).y > index_mcp(lms).y:
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if thumb_tip(lms).y > index_pip(lms).y and is_finger_open_sideways(thumb_tip(lms), thumb_ip(lms), handedness):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if is_finger_open_sideways(index_tip(lms), index_pip(lms), handedness):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if is_finger_closed_sideways(middle_tip(lms), middle_dip(lms), handedness):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed_sideways(ring_tip(lms), ring_dip(lms), handedness):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed_sideways(pinky_tip(lms), pinky_dip(lms), handedness):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_h(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_h(results, lms):
        text = 'H - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'H'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_hand_closed_sideways(results, lms) and wrist(lms).y > index_mcp(lms).y:
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if thumb_tip(lms).y > index_pip(lms).y and is_finger_open_sideways(thumb_tip(lms), thumb_ip(lms), handedness):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if is_finger_open_sideways(index_tip(lms), index_pip(lms), handedness):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if is_finger_open_sideways(middle_tip(lms), middle_dip(lms), handedness):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed_sideways(ring_tip(lms), ring_dip(lms), handedness):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed_sideways(pinky_tip(lms), pinky_dip(lms), handedness):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_i(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_i(results, lms):
        text = 'I - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'I'
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
            
        if is_finger_open(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_j(results, lms):
    pass

def module_k(results, lms):
    
    if is_letter_k(results, lms):
        text = 'K - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'K'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if (thumb_tip(lms).x > min(index_pip(lms).x, middle_pip(lms).x) and
            thumb_tip(lms).x < max(index_pip(lms).x, middle_pip(lms).x) and
            thumb_tip(lms).y < index_mcp(lms).y):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if (is_finger_open(index_tip(lms), index_pip(lms), wrist(lms)) and 
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms))):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if (is_finger_open(middle_tip(lms), middle_pip(lms), wrist(lms)) and  
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms))):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_l(results, lms):
    
    if is_letter_l(results, lms):
        text = 'L - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'L'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if abs(normalized_slope(index_mcp(lms), index_tip(lms))) - abs(normalized_slope(thumb_mcp(lms), thumb_tip(lms))) > 0.5:
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

def module_m(results, lms):
    
    if is_letter_m(results, lms):
        text = 'M - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'M'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if ring_pip(lms).y < thumb_tip(lms).y < pinky_pip(lms).y:
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

def module_n(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_n(results, lms):
        text = 'N - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'N'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if ((handedness and is_touching(thumb_tip(lms), middle_pip(lms), middle_dip(lms)) and
                is_touching(thumb_tip(lms), ring_pip(lms), ring_dip(lms)) and
                middle_pip(lms).y < thumb_tip(lms).y < ring_pip(lms).y and
                thumb_tip(lms).x < middle_pip(lms).x) or 
            (not handedness and is_touching(thumb_tip(lms), middle_pip(lms), middle_dip(lms)) and
                is_touching(thumb_tip(lms), ring_pip(lms), ring_dip(lms)) and
                middle_pip(lms).y < thumb_tip(lms).y < ring_pip(lms).y and
                thumb_tip(lms).x > middle_pip(lms).x)):
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

def module_o(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_o(results, lms):
        text = 'O - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'O'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if (not is_facing_forward(results, lms) and
            not is_facing_back_and_sideways(results, lms) and
            distance(index_mcp(lms), pinky_mcp(lms)) < 0.7 * distance(index_mcp(lms), wrist(lms)) and
            wrist(lms).y > index_mcp(lms).y):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if (is_touching(index_tip(lms), thumb_tip(lms), thumb_ip(lms)) and
            is_touching(middle_tip(lms), thumb_tip(lms), thumb_ip(lms)) and
            is_touching(ring_tip(lms), thumb_tip(lms), thumb_ip(lms)) and
            is_touching(pinky_tip(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if (((handedness and normalized_slope(index_tip(lms), index_pip(lms)) > -0.5) or
            (not handedness and normalized_slope(index_tip(lms), index_pip(lms)) < 0.5)) and 
            is_touching(index_tip(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if (((handedness and normalized_slope(middle_tip(lms), middle_pip(lms)) > -0.4) or
            (not handedness and normalized_slope(middle_tip(lms), middle_pip(lms)) < 0.4)) and
            is_touching(middle_tip(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if (((handedness and normalized_slope(ring_tip(lms), ring_pip(lms)) > -0.3) or
            (not handedness and normalized_slope(ring_tip(lms), ring_pip(lms)) < 0.3)) and
            is_touching(ring_tip(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if (((handedness and normalized_slope(pinky_tip(lms), pinky_pip(lms)) > -0.3) or
            (not handedness and normalized_slope(pinky_tip(lms), pinky_pip(lms)) < 0.3)) and
            is_touching(pinky_tip(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_p(results, lms):
    
    if is_letter_p(results, lms):
        text = 'P - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'P'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_back_upside_down(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if min(index_pip(lms).x, middle_pip(lms).x) < thumb_tip(lms).x < max(index_pip(lms).x, middle_pip(lms).x):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if (is_finger_open(index_tip(lms), index_pip(lms), wrist(lms)) and 
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms))):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if (is_finger_open(middle_tip(lms), middle_pip(lms), wrist(lms)) and 
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms))):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed(ring_tip(lms), ring_dip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed(pinky_tip(lms), pinky_dip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_q(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_q(results, lms):
        text = 'Q - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'Q'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_back_upside_down(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if (not is_touching_close(thumb_tip(lms), index_tip(lms), index_dip(lms)) and
            ((handedness and thumb_tip(lms).x < index_tip(lms).x) or
            (not handedness and thumb_tip(lms).x > index_tip(lms).x))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if (not is_touching_close(thumb_tip(lms), index_tip(lms), index_dip(lms)) and
            is_finger_open(index_tip(lms), index_pip(lms), wrist(lms))):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed(ring_tip(lms), ring_dip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed(pinky_tip(lms), pinky_dip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
        
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_r(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_r(results, lms):
        text = 'R - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'R'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
          
        if (is_touching(thumb_tip(lms), ring_dip(lms), ring_tip(lms)) or
            is_touching(thumb_tip(lms), ring_tip(lms), ring_dip(lms))): 
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if (is_finger_open(index_tip(lms), index_pip(lms), wrist(lms)) and
            is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)) and
            (handedness and index_tip(lms).x < middle_tip(lms).x) or 
            (not handedness and index_tip(lms).x > middle_tip(lms).x)):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if (is_finger_open(middle_tip(lms), middle_pip(lms), wrist(lms)) and
            is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)) and
            (handedness and index_tip(lms).x < middle_tip(lms).x) or 
            (not handedness and index_tip(lms).x > middle_tip(lms).x)):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_s(results, lms):
    left = min(index_tip(lms).x, index_pip(lms).x, pinky_tip(lms).x, pinky_pip(lms).x)
    right = max(index_tip(lms).x, index_pip(lms).x, pinky_tip(lms).x, pinky_pip(lms).x)
    top = min(index_tip(lms).y, index_pip(lms).y, pinky_tip(lms).y, pinky_pip(lms).y)
    bottom = max(index_tip(lms).y, index_pip(lms).y, pinky_tip(lms).y, pinky_pip(lms).y)
    
    if is_letter_s(results, lms):
        text = 'S - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'S'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if left < thumb_tip(lms).x < right and top < thumb_tip(lms).y < bottom:
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

def module_t(results, lms):
    
    if is_letter_t(results, lms):
        text = 'T - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'T'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if (thumb_tip(lms).x < max(index_pip(lms).x, middle_pip(lms).x) and
            thumb_tip(lms).x > min(index_pip(lms).x, middle_pip(lms).x)):
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

def module_u(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_u(results, lms):
        text = 'U - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'U'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
          
        if (is_touching_close(thumb_tip(lms), ring_dip(lms), ring_tip(lms)) or
            is_touching_close(thumb_tip(lms), ring_tip(lms), ring_dip(lms))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
                
        if (is_finger_open(index_tip(lms), index_pip(lms), wrist(lms)) and 
            is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)) and
            ((handedness and index_tip(lms).x > middle_tip(lms).x) or 
             (not handedness and index_tip(lms).x < middle_tip(lms).x))):
            hand_colors.set_index_color(hand_colors._GREEN)
          
        if (is_finger_open(middle_tip(lms), middle_pip(lms), wrist(lms)) and 
            is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)) and
            ((handedness and index_tip(lms).x > middle_tip(lms).x) or 
             (not handedness and index_tip(lms).x < middle_tip(lms).x))):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_v(results, lms):
    if is_letter_v(results, lms):
        text = 'V - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'V'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if (is_touching_close(thumb_tip(lms), ring_dip(lms), ring_tip(lms)) or
            is_touching_close(thumb_tip(lms), ring_tip(lms), ring_dip(lms))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if (is_finger_open(index_tip(lms), index_pip(lms), wrist(lms)) and 
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms))):
            hand_colors.set_index_color(hand_colors._GREEN)
  
        if (is_finger_open(middle_tip(lms), middle_pip(lms), wrist(lms)) and 
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms))):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_w(results, lms):
    if is_letter_w(results, lms):
        text = 'W - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'W'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
          
        
        if is_touching(pinky_tip(lms), thumb_tip(lms), thumb_mcp(lms)):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if (is_finger_open(index_tip(lms), index_pip(lms), wrist(lms)) and 
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms))):
            hand_colors.set_index_color(hand_colors._GREEN)
          
        if (is_finger_open(middle_tip(lms), middle_pip(lms), wrist(lms)) and 
            not is_touching(index_tip(lms), middle_tip(lms), middle_dip(lms)) and
            not is_touching(ring_tip(lms), middle_tip(lms), middle_dip(lms))):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if (is_finger_open(ring_tip(lms), ring_pip(lms), wrist(lms)) and
            not is_touching(ring_tip(lms), middle_tip(lms), middle_dip(lms))):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_closed(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_x(results, lms):
    
    if is_letter_x(results, lms):
        text = 'X - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'X'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if abs(normalized_slope(wrist(lms), middle_mcp(lms))) > 0.7:
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if (is_touching(thumb_tip(lms), middle_pip(lms), middle_dip(lms)) or
             is_touching(thumb_tip(lms), middle_dip(lms), middle_pip(lms))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if is_index_x(index_tip(lms), index_pip(lms), index_mcp(lms)):
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

def module_y(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_y(results, lms):
        text = 'Y - Correct!'
        text_color = correct_color
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'Y'
        text_color = idle_color
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
            
        if (((handedness and thumb_tip(lms).x > max(index_mcp(lms).x, index_dip(lms).x)) or
            (not handedness and thumb_tip(lms).x < min(index_mcp(lms).x, index_dip(lms).x))) and 
            not is_touching_far(index_mcp(lms), thumb_tip(lms), thumb_ip(lms))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
            
        if is_finger_closed(index_tip(lms), index_pip(lms), wrist(lms)):
            hand_colors.set_index_color(hand_colors._GREEN)
            
        if is_finger_closed(middle_tip(lms), middle_pip(lms), wrist(lms)):
            hand_colors.set_middle_color(hand_colors._GREEN)
            
        if is_finger_closed(ring_tip(lms), ring_pip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
            
        if is_finger_open(pinky_tip(lms), pinky_pip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
            
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

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