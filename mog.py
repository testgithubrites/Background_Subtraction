import cv2
# Load your video
cap = cv2.VideoCapture(0)
# Create a smart background model
background = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    if not ret:
        break
   # Ask the model: what part of this frame is moving?
    fg_mask = background.apply(frame)
    # Show the moving parts (white = motion, black = background)
    cv2.imshow("Motion Detection", fg_mask)
    if cv2.waitKey(30) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
