import cv2
import numpy as np
cap = cv2.VideoCapture("video.mp4")
ret , frame = cap.read()
avg = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY).astype("float")
alpha = 0.05
while True:
    ret , frame = cap.read()
    if not ret:
      break
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    #Update the running average
    cv2.accumulateWeighted(gray,avg,alpha)
    #Compute the difference between background image and current frame
    background = cv2.convertScaleAbs(avg) #converts float to int and takes absolute values
    diff = cv2.absdiff(gray, background)
    _, thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)
    cv2.imshow("Foreground Mask", thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()