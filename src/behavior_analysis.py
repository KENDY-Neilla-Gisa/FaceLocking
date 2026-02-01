# Behavior Analysis Module
# This module provides functions for detecting basic facial behaviors
# using landmark positions from MediaPipe FaceMesh

# Global variables for tracking state across frames
previous_nose_position = None
wink_detection_count = 0

def analyze_head_motion(nose_coordinate, motion_threshold):
    """
    Analyzes horizontal head movement based on nose position changes.
    
    Args:
        nose_coordinate: Current nose X coordinate
        motion_threshold: Minimum pixel movement to register as motion
        
    Returns:
        String describing detected motion or None
    """
    global previous_nose_position
    detected_action = None

    if previous_nose_position is not None:
        position_change = nose_coordinate - previous_nose_position
        if position_change > motion_threshold:
            detected_action = "Head Moved Right"
        elif position_change < -motion_threshold:
            detected_action = "Head Moved Left"

    previous_nose_position = nose_coordinate
    return detected_action


def analyze_eye_closure(upper_eye, lower_eye, closure_threshold):
    """
    Detects eye blinking by monitoring eye openness ratio.
    
    Args:
        upper_eye: Upper eye landmark coordinates
        lower_eye: Lower eye landmark coordinates  
        closure_threshold: Minimum eye openness ratio to consider eyes open
        
    Returns:
        String describing blink detection or None
    """
    global wink_detection_count
    eye_openness = abs(upper_eye[1] - lower_eye[1])

    if eye_openness < closure_threshold:
        wink_detection_count += 1
    else:
        if wink_detection_count > 2:
            wink_detection_count = 0
            return "Eye Blink Detected"
        wink_detection_count = 0
    return None


def analyze_facial_expression(left_mouth, right_mouth, expression_threshold):
    """
    Detects smiling by analyzing mouth corner distance.
    
    Args:
        left_mouth: Left mouth corner landmark coordinates
        right_mouth: Right mouth corner landmark coordinates
        expression_threshold: Minimum mouth width to register as smile
        
    Returns:
        String describing smile detection or None
    """
    mouth_span = abs(right_mouth[0] - left_mouth[0])
    if mouth_span > expression_threshold:
        return "Smile Detected"
    return None
