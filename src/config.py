# Intelligent Identity Tracking System Configuration
# This file contains all adjustable parameters for the tracking system

# Target user for identity tracking (must match enrolled name exactly)
TARGET_USER = "User_01"

# Minimum confidence score required to establish identity tracking
CONFIDENCE_THRESHOLD = 0.65

# Maximum consecutive frames without target detection before releasing tracking
MAX_MISSING_FRAMES = 25

# Sensitivity thresholds for behavior detection
HEAD_MOVEMENT_SENSITIVITY = 10      # Pixels of nose movement required
SMILE_DETECTION_THRESHOLD = 45       # Mouth corner distance in pixels
BLINK_DETECTION_THRESHOLD = 2.8      # Eye openness ratio
