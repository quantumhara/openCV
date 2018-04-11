import cv2
import numpy as np

cap = cv2.VideoCapture('small.mp4')
frame_counter = 0

fps = 60

print "press 'q' to quit"

n=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame_counter += 1
    #If the last frame is reached, reset the capture and the frame_counter
    if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_counter = 0 #Or whatever as long as it is the same as next line
        cap.set(cv2.CAP_PROP_POS_FRAMES, 60)
    # Our operations on the frame come here
    # Display the resulting frame
    cv2.imshow('frame', frame)
    n=n+1
    if cv2.waitKey(fps) & 0xFF == ord('q'):
        break
    # When everything done, release the capture
    print "n=", n

cap.release()
cv2.destroyAllWindows()
