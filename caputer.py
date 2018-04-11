import numpy as np
import cv2

cap = cv2.VideoCapture(1) # video capture source camera (Here webcam of laptop)
ret,frame = cap.read() # return a single frame in variable `frame`

print 'save on pressing "y"'

while(True):
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
        cv2.imwrite('image.png',frame)
        cv2.destroyAllWindows()
        break

cap.release()
