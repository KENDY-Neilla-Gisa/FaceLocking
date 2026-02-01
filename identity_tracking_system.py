import cv2
from src.config import *
from src.face_lock import IdentityTracker
from src.behavior_analysis import *
from src.event_recorder import ActionRecorder

from src.recognize import recognize_faces   # your existing function

identity_tracker = IdentityTracker(TARGET_USER, MAX_MISSING_FRAMES)
action_recorder = None

camera_feed = cv2.VideoCapture(0)

while True:
    frame_success, current_frame = camera_feed.read()
    if not frame_success:
        break

    # Your recognition returns multiple faces
    detected_faces = recognize_faces(current_frame)
    print("Detected faces:", detected_faces)

    # Expected format per face:
    # {
    #   "name": identity_name,
    #   "similarity": similarity_score,
    #   "bbox": (x1,y1,x2,y2),
    #   "landmarks": [left_eye, right_eye, nose, mouth_left, mouth_right]
    # }

    for face_data in detected_faces:
        person_name = face_data["name"]
        match_confidence = face_data["similarity"]
        face_region = face_data["bbox"]
        facial_landmarks = face_data["landmarks"]

        tracking_initiated = identity_tracker.initiate_tracking(person_name, match_confidence, CONFIDENCE_THRESHOLD, face_region)

        if tracking_initiated and action_recorder is None:
            action_recorder = ActionRecorder(person_name)

        identity_tracker.update_tracking(person_name, face_region)

        if identity_tracker.tracking_active and person_name == identity_tracker.tracked_id:
            left_eye_pt, right_eye_pt, nose_pt, mouth_left_pt, mouth_right_pt = facial_landmarks

            head_motion = analyze_head_motion(nose_pt[0], HEAD_MOVEMENT_SENSITIVITY)
            eye_blink = analyze_eye_closure(left_eye_pt, right_eye_pt, BLINK_DETECTION_THRESHOLD)
            smile_action = analyze_facial_expression(mouth_left_pt, mouth_right_pt, SMILE_DETECTION_THRESHOLD)

            for detected_action in [head_motion, eye_blink, smile_action]:
                if detected_action:
                    print("[ACTION]", detected_action)
                    action_recorder.record_event(detected_action)

            cv2.putText(current_frame, "TRACKING ACTIVE", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Identity Tracking System", current_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera_feed.release()
cv2.destroyAllWindows()
