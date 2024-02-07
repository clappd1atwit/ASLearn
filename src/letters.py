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
    
    # Right Hand
    if handedness:
        if is_hand_closed(landmarks) and thumb_tip.y < thumb_mcp.y and thumb_tip.x > index_mcp.x:
            return 'A'
        else:
            return 'Not A'
    # Left Hand
    else:
        if is_hand_closed(landmarks) and thumb_tip.y < thumb_mcp.y and thumb_tip.x < index_mcp.x:
            return 'A'
        else:
            return 'Not A'