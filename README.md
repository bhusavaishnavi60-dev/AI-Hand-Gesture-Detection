# AI Hand Gesture Detection using MediaPipe & OpenCV

## Project Description

This is a Computer Vision and Artificial Intelligence (AIML) project that detects human hands in real time using a webcam. It identifies 21 hand landmarks, detects left and right hands, recognizes finger states and hand gestures, and displays the results live on the screen.

## Aim of the Project

To build a real-time hand gesture recognition system using MediaPipe and OpenCV that can detect hand landmarks and identify different hand gestures through a webcam.

## Technologies Used

* Python
* OpenCV
* MediaPipe

## Features

* Real-time hand detection using webcam.
* Detect one or two hands.
* Track 21 hand landmarks.
* Detect Left and Right hand.
* Detect finger states (`[1,1,0,0,0]` format).
* Count fingers (0–5).
* Recognize gestures:

  * Open Hand
  * Closed Hand
  * Peace ✌️
  * Thumbs Up 👍

## Project Structure

hand_gesture/
├── app.py
├── anime_avatar.py *(optional extension)*
├── requirements.txt
├── README.md
└── assets/
└── anime_hand.png

## How to Run

1. Install the required libraries.

```bash
pip install -r requirements.txt
```

2. Run the project.

```bash
python app.py
```

3. Press **Q** to close the webcam.

## Output

* Displays 21 hand landmarks.
* Shows Left or Right hand.
* Shows detected gesture.
* Prints finger states in the terminal.

## Future Enhancements

* Anime avatar motion tracking.
* Volume control using hand gestures.
* Air drawing using fingers.
* Sign language recognition.

