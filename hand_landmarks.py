import mediapipe as mp

# hand_landmarks.py creates a simplified way of calling the mediapipe hand tracking 
# locations defined here: https://developers.google.com/mediapipe/solutions/vision/hand_landmarker.
# Each function has its corresponding index commented above the function definition, takes the set
# of all landmarks, and returns the specific landmark needed.

#0
def wrist(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.WRIST]

#1
def thumb_cmc(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_CMC]

#2
def thumb_mcp(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_MCP]

#3
def thumb_ip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_IP]

#4
def thumb_tip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]

#5
def index_mcp(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]

#6
def index_pip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_PIP]

#7
def index_dip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_DIP]

#8
def index_tip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]

#9
def middle_mcp(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_MCP]

#10
def middle_pip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_PIP]

#11
def middle_dip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_DIP]

#12
def middle_tip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]

#13
def ring_mcp(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_MCP]

#14
def ring_pip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_PIP]

#15
def ring_dip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_DIP]

#16
def ring_tip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP]

#17
def pinky_mcp(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_MCP]

#18
def pinky_pip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_PIP]

#19
def pinky_dip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_DIP]

#20
def pinky_tip(landmarks):
    return landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP]
