import mediapipe as mp
from helpers import *

def is_letter_a(results, landmarks):
    handedness = is_right_hand(results, landmarks)
    thumb_tip = landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
    thumb_mcp = landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_MCP]
    index_mcp = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    if handedness:
        if not is_hand_open(landmarks) and thumb_tip.y < thumb_mcp.y and thumb_tip.x > index_mcp.x:
            return 'A'
        else:
            return 'Not A'
    else:
        if not is_hand_open(landmarks) and thumb_tip.y < thumb_mcp.y and thumb_tip.x < index_mcp.x:
            return 'A'
        else:
            return 'Not A'