import cv2
import numpy as np

img = cv2.imread('image2.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

rho = 1
theta = np.pi / 180
threshold = 15
min_line_length = 50
max_line_gap = 20
line_image = np.copy(img) * 0

lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)
#print(lines)
points = []

font = cv2.FONT_HERSHEY_SIMPLEX

i=0
for line in lines:
    for x1, y1, x2, y2 in line:
        points.append(((x1 + 0.0, y1 + 0.0), (x2 + 0.0, y2 + 0.0)))
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 5)
        cv2.putText(img, 'line{}'.format(i), (x1, y1), font, 0.8,(200,200,255), 2)
        a=(y2-y1)/(x2-x1)
        b=(x2*y1-y2*x2)/(x2-x1)
        i=i+1
        print "line"+str(i)+" a,b=",  a, b, "  x,y=",x1, x2, y1, y2


# drawing line
lineThickness = 20
cv2.line(img, (2000, 2000), (10, 10), (20,20,200), lineThickness)

lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)
print(lines_edges.shape)

cv2.imwrite('line_parking.png', lines_edges)
