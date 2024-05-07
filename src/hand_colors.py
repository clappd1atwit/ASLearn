from typing import Mapping, Tuple

import mediapipe as mp
from mediapipe.python.solutions.drawing_utils import DrawingSpec
from mediapipe.python.solutions.hands import HandLandmark
from mediapipe.python.solutions import hands_connections


_RADIUS = 5
_RED = (48, 48, 255)
_GREEN = (48, 255, 48)

# Hands
_THICKNESS_WRIST_MCP = 3
_THICKNESS_FINGER = 2
_THICKNESS_DOT = -1

# Hand landmarks
_PALM_LANDMARKS = (HandLandmark.WRIST, HandLandmark.THUMB_CMC,
                   HandLandmark.INDEX_FINGER_MCP,
                   HandLandmark.MIDDLE_FINGER_MCP, HandLandmark.RING_FINGER_MCP,
                   HandLandmark.PINKY_MCP)
_THUMB_LANDMARKS = (HandLandmark.THUMB_MCP, HandLandmark.THUMB_IP,
                    HandLandmark.THUMB_TIP)
_INDEX_FINGER_LANDMARKS = (HandLandmark.INDEX_FINGER_PIP,
                           HandLandmark.INDEX_FINGER_DIP,
                           HandLandmark.INDEX_FINGER_TIP)
_MIDDLE_FINGER_LANDMARKS = (HandLandmark.MIDDLE_FINGER_PIP,
                            HandLandmark.MIDDLE_FINGER_DIP,
                            HandLandmark.MIDDLE_FINGER_TIP)
_RING_FINGER_LANDMARKS = (HandLandmark.RING_FINGER_PIP,
                          HandLandmark.RING_FINGER_DIP,
                          HandLandmark.RING_FINGER_TIP)
_PINKY_FINGER_LANDMARKS = (HandLandmark.PINKY_PIP, HandLandmark.PINKY_DIP,
                           HandLandmark.PINKY_TIP)

incorrect_color = DrawingSpec(
            color=_RED, thickness=_THICKNESS_DOT, circle_radius=_RADIUS)
correct_color = DrawingSpec(
            color=_GREEN, thickness=_THICKNESS_DOT, circle_radius=_RADIUS)

incorrect_color_finger = DrawingSpec(
            color=_RED, thickness=_THICKNESS_FINGER, circle_radius=_RADIUS)
correct_color_finger = DrawingSpec(
            color=_GREEN, thickness=_THICKNESS_FINGER, circle_radius=_RADIUS)

# Hands connections
_HAND_CONNECTION_STYLE = {
    hands_connections.HAND_PALM_CONNECTIONS:
        DrawingSpec(color=_RED, thickness=_THICKNESS_WRIST_MCP),
    hands_connections.HAND_THUMB_CONNECTIONS:
        DrawingSpec(color=_RED, thickness=_THICKNESS_FINGER),
    hands_connections.HAND_INDEX_FINGER_CONNECTIONS:
        DrawingSpec(color=_RED, thickness=_THICKNESS_FINGER),
    hands_connections.HAND_MIDDLE_FINGER_CONNECTIONS:
        DrawingSpec(color=_RED, thickness=_THICKNESS_FINGER),
    hands_connections.HAND_RING_FINGER_CONNECTIONS:
        DrawingSpec(color=_RED, thickness=_THICKNESS_FINGER),
    hands_connections.HAND_PINKY_FINGER_CONNECTIONS:
        DrawingSpec(color=_RED, thickness=_THICKNESS_FINGER)
}

_HAND_LANDMARK_STYLE = {
    _PALM_LANDMARKS: incorrect_color,
    _THUMB_LANDMARKS: incorrect_color,
    _INDEX_FINGER_LANDMARKS: incorrect_color,
    _MIDDLE_FINGER_LANDMARKS: incorrect_color,
    _RING_FINGER_LANDMARKS: incorrect_color,
    _PINKY_FINGER_LANDMARKS: incorrect_color,
}

def get_incorrect_hand_landmarks_style() -> Mapping[int, DrawingSpec]:
  """Returns the default hand landmarks drawing style.

  Returns:
      A mapping from each hand landmark to its default drawing spec.
  """
  hand_landmark_style = {}
  for k, v in _HAND_LANDMARK_STYLE.items():
    for landmark in k:
      _HAND_LANDMARK_STYLE[k] = incorrect_color
      hand_landmark_style[landmark] = incorrect_color
  return hand_landmark_style

def get_correct_hand_landmarks_style() -> Mapping[int, DrawingSpec]:
  """Returns the default hand landmarks drawing style.

  Returns:
      A mapping from each hand landmark to its default drawing spec.
  """
  hand_landmark_style = {}
  for k, v in _HAND_LANDMARK_STYLE.items():
    for landmark in k:
      _HAND_LANDMARK_STYLE[k] = correct_color
      hand_landmark_style[landmark] = correct_color
  return hand_landmark_style

def get_current_hand_landmarks_style() -> Mapping[int, DrawingSpec]:
  """Returns the default hand landmarks drawing style.

  Returns:
      A mapping from each hand landmark to its default drawing spec.
  """
  hand_landmark_style = {}
  for k, v in _HAND_LANDMARK_STYLE.items():
    for landmark in k:
      hand_landmark_style[landmark] = v
  return hand_landmark_style

def get_incorrect_hand_connections_style(
) -> Mapping[Tuple[int, int], DrawingSpec]:
  """Returns the default hand connections drawing style.

  Returns:
      A mapping from each hand connection to its default drawing spec.
  """
  hand_connection_style = {}
  for k, v in _HAND_CONNECTION_STYLE.items():
    for connection in k:
        _HAND_CONNECTION_STYLE[k] = incorrect_color_finger
        hand_connection_style[connection] = incorrect_color_finger
  return hand_connection_style

def get_correct_hand_connections_style(
) -> Mapping[Tuple[int, int], DrawingSpec]:
  """Returns the default hand connections drawing style.

  Returns:
      A mapping from each hand connection to its default drawing spec.
  """
  hand_connection_style = {}
  for k, v in _HAND_CONNECTION_STYLE.items():
    for connection in k:
        _HAND_CONNECTION_STYLE[k] = correct_color_finger
        hand_connection_style[connection] = correct_color_finger
  return hand_connection_style

def get_current_hand_connections_style(
) -> Mapping[Tuple[int, int], DrawingSpec]:
  """Returns the default hand connections drawing style.

  Returns:
      A mapping from each hand connection to its default drawing spec.
  """
  hand_connection_style = {}
  for k, v in _HAND_CONNECTION_STYLE.items():
    for connection in k:
      hand_connection_style[connection] = v
  return hand_connection_style


def set_palm_color(color):
    _HAND_LANDMARK_STYLE[_PALM_LANDMARKS] = DrawingSpec(
            color=color, thickness=_THICKNESS_DOT, circle_radius=_RADIUS)
    _HAND_CONNECTION_STYLE[hands_connections.HAND_PALM_CONNECTIONS] = DrawingSpec(
            color=color, thickness=_THICKNESS_FINGER, circle_radius=_RADIUS)
    
def set_thumb_color(color):
    _HAND_LANDMARK_STYLE[_THUMB_LANDMARKS] = DrawingSpec(
            color=color, thickness=_THICKNESS_DOT, circle_radius=_RADIUS)   
    _HAND_CONNECTION_STYLE[hands_connections.HAND_THUMB_CONNECTIONS] = DrawingSpec(
            color=color, thickness=_THICKNESS_FINGER, circle_radius=_RADIUS)
   
def set_index_color(color):
    _HAND_LANDMARK_STYLE[_INDEX_FINGER_LANDMARKS] = DrawingSpec(
            color=color, thickness=_THICKNESS_DOT, circle_radius=_RADIUS)   
    _HAND_CONNECTION_STYLE[hands_connections.HAND_INDEX_FINGER_CONNECTIONS] = DrawingSpec(
            color=color, thickness=_THICKNESS_FINGER, circle_radius=_RADIUS)
    
def set_middle_color(color):
    _HAND_LANDMARK_STYLE[_MIDDLE_FINGER_LANDMARKS] = DrawingSpec(
            color=color, thickness=_THICKNESS_DOT, circle_radius=_RADIUS)
    _HAND_CONNECTION_STYLE[hands_connections.HAND_MIDDLE_FINGER_CONNECTIONS] = DrawingSpec(
            color=color, thickness=_THICKNESS_FINGER, circle_radius=_RADIUS)
    
def set_ring_color(color):
    _HAND_LANDMARK_STYLE[_RING_FINGER_LANDMARKS] = DrawingSpec(
            color=color, thickness=_THICKNESS_DOT, circle_radius=_RADIUS)
    _HAND_CONNECTION_STYLE[hands_connections.HAND_RING_FINGER_CONNECTIONS] = DrawingSpec(
            color=color, thickness=_THICKNESS_FINGER, circle_radius=_RADIUS)
    
def set_pinky_color(color):
    _HAND_LANDMARK_STYLE[_PINKY_FINGER_LANDMARKS] = DrawingSpec(
            color=color, thickness=_THICKNESS_DOT, circle_radius=_RADIUS)
    _HAND_CONNECTION_STYLE[hands_connections.HAND_PINKY_FINGER_CONNECTIONS] = DrawingSpec(
            color=color, thickness=_THICKNESS_FINGER, circle_radius=_RADIUS)