import cv2
import mediapipe as mp
import time

<<<<<<< HEAD
# init camera objectf
=======
# init camera object
>>>>>>> db0bf2e4fad61b9db3a1a30ec35b6523179bd353
cap=cv2.VideoCapture(0)

while True:
    # read frame from camera
    success,img=cap.read()

    if success:
        # show frame in window if reading was successful
        cv2.imshow("Camera Feed",img)
        

    # wait for pressing ESC to break the loop
    if cv2.waitKey(1) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
