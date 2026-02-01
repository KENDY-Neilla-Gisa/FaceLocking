# Event Recording Module
# This module handles the logging of detected behaviors to timestamped files

from datetime import datetime

class ActionRecorder:
    """
    Records facial behavior events to timestamped log files.
    
    Attributes:
        log_file: File handle for writing events
        user_identifier: Name of the tracked user
    """
    def __init__(self, user_identifier):
        """
        Initialize the event recorder with a timestamped log file.
        
        Args:
            user_identifier: Name of the person being tracked
        """
        current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        log_filename = f"{user_identifier.lower()}_actions_{current_timestamp}.txt"
        self.log_file = open(log_filename, "w")
        self.user_identifier = user_identifier
        print(f"[ACTION LOG INITIALIZED] {log_filename}")

    def record_event(self, action_type, details=""):
        """
        Log a detected behavior event with timestamp.
        
        Args:
            action_type: Description of the detected behavior
            details: Additional information about the event (optional)
        """
        event_time = datetime.now().strftime("%H:%M:%S")
        self.log_file.write(f"{event_time} | {action_type} | {details}\n")
        self.log_file.flush()
