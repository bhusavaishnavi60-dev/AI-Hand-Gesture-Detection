import cv2
import mediapipe as mp

# ------------------------------------
# STEP 1 : OPEN WEBCAM
# ------------------------------------
camera = cv2.VideoCapture(0)

# ------------------------------------
# STEP 2 : LOAD MEDIAPIPE HAND MODEL
# ------------------------------------
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Draw landmarks
mp_draw = mp.solutions.drawing_utils

# Finger tip landmark IDs
tips = [4, 8, 12, 16, 20]

# Store previous finger state (so terminal doesn't print repeatedly)
previous_state = None

# ------------------------------------
# STEP 3 : START CAMERA LOOP
# ------------------------------------
while True:

    success, frame = camera.read()

    if not success:
        break

    # Mirror camera
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb)

    # ------------------------------------
    # STEP 4 : IF HAND FOUND
    # ------------------------------------
    if results.multi_hand_landmarks:

        for hand_landmarks, handedness in zip(
                results.multi_hand_landmarks,
                results.multi_handedness):

            # ------------------------------------
            # LEFT OR RIGHT HAND
            # ------------------------------------
            label = handedness.classification[0].label

            cv2.putText(
                frame,
                f"{label} Hand",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # ------------------------------------
            # FINGER STATES
            # Order:
            # [Thumb, Index, Middle, Ring, Little]
            # ------------------------------------
            fingers = []

            # Thumb
            if label == "Right":
                if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:   # Left Hand
                if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # Index, Middle, Ring, Little
            for tip in tips[1:]:
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # ------------------------------------
            # PRINT FINGER STATES IN TERMINAL
            # ------------------------------------
            if fingers != previous_state:
                print("Finger States:", fingers)
                previous_state = fingers.copy()

            # Count fingers
            total_fingers = fingers.count(1)

            # ------------------------------------
            # GESTURE RECOGNITION
            # ------------------------------------
            gesture = "Unknown"

            if fingers == [1, 1, 1, 1, 1]:
                gesture = "Open Hand"

            elif fingers == [0, 0, 0, 0, 0]:
                gesture = "Closed Hand"

            elif fingers == [0, 1, 1, 0, 0]:
                gesture = "Peace"

            elif fingers == [1, 0, 0, 0, 0]:
                gesture = "Thumbs Up"

            elif fingers == [0, 1, 0, 0, 0]:
                gesture = "One Finger"

            # ------------------------------------
            # SHOW GESTURE ON SCREEN
            # ------------------------------------
            cv2.putText(
                frame,
                f"Gesture : {gesture}",
                (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

            # ------------------------------------
            # SHOW TOTAL FINGERS ON SCREEN
            # ------------------------------------
            cv2.putText(
                frame,
                f"Fingers : {total_fingers}",
                (10, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

    # ------------------------------------
    # STEP 5 : SHOW OUTPUT
    # ------------------------------------
    cv2.imshow("AI Hand Gesture Detection", frame)

    # Press Q to Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ------------------------------------
# STEP 6 : CLOSE CAMERA
# ------------------------------------
camera.release()
cv2.destroyAllWindows()