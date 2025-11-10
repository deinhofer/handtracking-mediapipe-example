import cv2
import mediapipe as mp
import time

# init mediapipe Hands solution
mpHands=mp.solutions.hands
hands=mpHands.Hands(model_complexity=0, min_tracking_confidence=0.5,min_detection_confidence=0.5)
mpDraw=mp.solutions.drawing_utils

# init camera object
cap=cv2.VideoCapture(0)

while True:
    # read frame from camera
    success,img=cap.read()

    if success:
        # convert colour
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        results=hands.process(imgRGB)

        if results.multi_hand_landmarks:
            # show frame in window if reading was successful
            for handLMS in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img,handLMS,mpHands.HAND_CONNECTIONS)

        cv2.imshow("Hand Tracking",img)

    # wait for pressing ESC to break the loop
    if cv2.waitKey(1) == 27:
        break
