import mediapipe as mp
import numpy as np

def is_hand_open(landmarks):
    # Define the indices for the thumb and index finger landmarks
    wrist = landmarks.landmark[mp.solutions.hands.HandLandmark.WRIST]
    
    index_finger_mcp = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    index_finger_tip = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    
    middle_finger_mcp = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    middle_finger_tip = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    
    ring_finger_mcp = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    ring_finger_tip = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    
    pinky_mcp = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]
    pinky_tip = landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]

    # Calculate the distance between thumb tip and index finger tip
    index_distance = distance(index_finger_mcp, index_finger_tip)
    middle_distance = distance(middle_finger_mcp, middle_finger_tip)
    ring_distance = distance(ring_finger_mcp, ring_finger_tip)
    pinky_distance = distance(pinky_mcp, pinky_tip)
    
    finger_data = np.array([index_distance, middle_distance, ring_distance, pinky_distance])
   
    avg_distance = np.mean(finger_data)
    finger_variance = np.std(finger_data)
    print(finger_variance)

    threshold = distance(wrist, index_finger_mcp) / 3

    return avg_distance > threshold

def is_right_hand(results, landmarks):
    return results.multi_handedness[
                results.multi_hand_landmarks.index(landmarks)
            ].classification[0].label == 'Left'
    
def distance(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5