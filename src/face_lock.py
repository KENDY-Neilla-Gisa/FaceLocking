# Identity Tracking Module
# This module implements the core logic for persistent identity tracking

class IdentityTracker:
    """
    Manages persistent tracking of a specific user across video frames.
    
    This class implements the core "identity tracking" functionality by maintaining
    tracking state even during brief periods of recognition failure.
    
    Attributes:
        target_user (str): Name of the user to track
        tracking_active (bool): Whether tracking is currently active
        tracked_id (str): ID of the currently tracked person
        missing_count (int): Consecutive frames without target detection
        max_missing (int): Threshold for releasing tracking
        tracked_region (tuple): Bounding box of tracked face
    """
    def __init__(self, target_user, max_missing=30):
        """
        Initialize the identity tracker.
        
        Args:
            target_user: Name of the user to track
            max_missing: Maximum frames without detection before releasing tracking
        """
        self.target_user = target_user
        self.tracking_active = False
        self.tracked_id = None
        self.missing_count = 0
        self.max_missing = max_missing
        self.tracked_region = None

    def initiate_tracking(self, person_id, confidence_score, min_confidence, region):
        if not self.tracking_active:
            if person_id == self.target_user and confidence_score > min_confidence:
                self.tracking_active = True
                self.tracked_id = person_id
                self.tracked_region = region
                print(f"[TRACKING STARTED] {person_id}")
                return True
        return False

    def update_tracking(self, person_id, region):
        if not self.tracking_active:
            return False

        if person_id == self.tracked_id:
            self.tracked_region = region
            self.missing_count = 0
        else:
            self.missing_count += 1

        if self.missing_count > self.max_missing:
            print("[TRACKING ENDED] Target lost")
            self.tracking_active = False
            self.tracked_id = None
            return False

        return True
