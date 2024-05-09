from helpers import *
from letters import *
import hand_colors

def module_a(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_a(results, lms):
        text = 'A - Correct!'
        text_color = (0, 200, 0)
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
    else:
        text = 'A'
        text_color = (255, 50, 255)
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
        if ((handedness and thumb_tip(lms).x > max(index_mcp(lms).x, index_dip(lms).x) and 
            (normalized_slope(thumb_mcp(lms), thumb_tip(lms)) > .7 or
            normalized_slope(thumb_mcp(lms), thumb_tip(lms)) < -.7)) or 
            (not handedness and thumb_tip(lms).x < min(index_mcp(lms).x, index_dip(lms).x) and 
            (normalized_slope(thumb_mcp(lms), thumb_tip(lms)) > .7 or
            normalized_slope(thumb_mcp(lms), thumb_tip(lms)) < -.7))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
        if is_finger_closed(index_tip(lms), index_dip(lms), wrist(lms)):
            hand_colors.set_index_color(hand_colors._GREEN)
        if is_finger_closed(middle_tip(lms), middle_dip(lms), wrist(lms)):
            hand_colors.set_middle_color(hand_colors._GREEN)
        if is_finger_closed(ring_tip(lms), ring_dip(lms), wrist(lms)):
            hand_colors.set_ring_color(hand_colors._GREEN)
        if is_finger_closed(pinky_tip(lms), pinky_dip(lms), wrist(lms)):
            hand_colors.set_pinky_color(hand_colors._GREEN)
        landmarks_color = hand_colors.get_current_hand_landmarks_style()
        connections_color = hand_colors.get_current_hand_connections_style()
        
    return text, text_color, landmarks_color, connections_color

def module_b(results, lms):
    handedness = is_right_hand(results, lms)
    
    if is_letter_b(results, lms):
        text = 'B - Correct!'
        text_color = (0, 200, 0)
        landmarks_color = hand_colors.get_correct_hand_landmarks_style()
        connections_color = hand_colors.get_correct_hand_connections_style()
        
    else:
        text = 'B'
        text_color = (255, 50, 255)
        hand_colors.get_incorrect_hand_landmarks_style()
        hand_colors.get_incorrect_hand_connections_style()

        if is_facing_forward(results, lms):
            hand_colors.set_palm_color(hand_colors._GREEN)
        if ((handedness and thumb_ip(lms).x - thumb_tip(lms).x > abs(thumb_tip(lms).y - thumb_ip(lms).y)) or 
            (not handedness and thumb_tip(lms).x - thumb_ip(lms).x > abs(thumb_tip(lms).y - thumb_ip(lms).y))):
            hand_colors.set_thumb_color(hand_colors._GREEN)
        if is_finger_open(index_tip(lms), index_pip(lms), wrist(lms)):
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

def module_c(results, lms):
    pass

def module_d(results, lms):
    pass

def module_e(results, lms):
    pass

def module_f(results, lms):
    pass

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