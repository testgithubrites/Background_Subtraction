import cv2
cap = cv2.VideoCapture(0)
ret , prev_frame = cap.read()
prev_frame = cv2.cvtColor(prev_frame , cv2.COLOR_BGR2GRAY)
prev_frame = cv2.GaussianBlur(prev_frame, (5, 5), 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
while True:
     ret , curr_frame = cap.read()
     gray = cv2.cvtColor(curr_frame , cv2.COLOR_BGR2GRAY)
     gray = cv2.GaussianBlur(gray , (5 , 5) , 0)
     diff = cv2.absdiff(gray , prev_frame)
     _ , thresh = cv2.threshold(diff , 50 , 255 , cv2.THRESH_BINARY)
     thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
     thresh = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, kernel)
     laplacian = cv2.Laplacian(gray, cv2.CV_64F)
     laplacian = cv2.convertScaleAbs(laplacian)
     motion_edges = cv2.bitwise_and(laplacian, laplacian, mask=thresh)
     glowing_edges = cv2.bitwise_not(motion_edges)
     cv2.imshow("Motion Edge Glow", glowing_edges)
     prev_frame = gray.copy()
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()