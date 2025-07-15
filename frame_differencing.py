import cv2
cap = cv2.VideoCapture(0)
ret , prev_frame = cap.read()
prev_frame = cv2.cvtColor(prev_frame , cv2.COLOR_BGR2GRAY)
prev_frame = cv2.GaussianBlur(prev_frame, (5, 5), 0)
while True:
     ret , curr_frame = cap.read()
     gray = cv2.cvtColor(curr_frame , cv2.COLOR_BGR2GRAY)
     gray = cv2.GaussianBlur(gray , (5 , 5) , 0)
     #Subtract frames
     diff = cv2.absdiff(gray , prev_frame)
     _ , thresh = cv2.threshold(diff , 50 , 255 , cv2.THRESH_BINARY)
     cv2.imshow("Motion" , thresh)
     prev_frame = gray.copy() #Update previous frame
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()