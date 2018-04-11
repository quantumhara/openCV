import cv2
import numpy as np

img = cv2.imread('image2.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

font = cv2.FONT_HERSHEY_SIMPLEX

lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[8]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.putText(img, 'line', (x1, y1), font, 0.8,(255,255,255),2,cv2.LINE_AA)


cv2.imwrite('houghlines3.jpg',img)
