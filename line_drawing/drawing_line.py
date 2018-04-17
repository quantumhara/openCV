import cv2
import numpy as np

# input
x_res = 1980
y_res = 1080

x11, y11, x12, y12 = 0, 200, 100, 300
x21, y21, x22, y22 = 20, 220, 120, 320
x31, y31, x32, y32 = 40, 240, 140, 340
x41, y41, x42, y42 = 60, 280, 160, 380
x51, y51, x52, y52 = 80, 320, 180, 420
x61, y61, x62, y62 = 100, 360, 200, 460



# main program
img = cv2.imread('image.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

low_threshold, high_threshold = 50, 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

rho, theta = 1, np.pi / 180
threshold = 15
min_line_length, max_line_gap = 50, 20
line_image = np.copy(img) * 0

lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
points = []

font = cv2.FONT_HERSHEY_SIMPLEX
lineThickness = 20


# shifting for y-axis
y11, y12 =- y11 + y_res, - y12 + y_res
y21, y22 =- y21 + y_res, - y22 + y_res
y31, y32 =- y31 + y_res, - y32 + y_res
y41, y42 =- y41 + y_res, - y42 + y_res
y51, y52 =- y51 + y_res, - y52 + y_res
y61, y62 =- y61 + y_res, - y62 + y_res


# drawing line
cv2.line(line_image, (x11, y11), (x12, y12), (100, 0, 0), 5)
cv2.putText(img, 'line{}'.format(1), (x11, y11), font, 0.8,(0,0,0), 2)
print x11, y11, x12, y12

# drawing line
cv2.line(line_image, (x21, y21), (x22, y22), (0, 100, 0), 5)
cv2.putText(img, 'line{}'.format(2), (x21, y21), font, 0.8,(0,0,0), 2)
print x21, y21, x22, y22

# drawing line
cv2.line(line_image, (x31, y31), (x32, y32), (0, 0, 100), 5)
cv2.putText(img, 'line{}'.format(3), (x31, y31), font, 0.8,(0, 0, 0), 2)
print x31, y31, x32, y32

# drawing line
cv2.line(line_image, (x41, y41), (x42, y42), (200, 50, 50), 5)
cv2.putText(img, 'line{}'.format(4), (x41, y41), font, 0.8,(0,0,0), 2)
print x41, y41, x42, y42

# drawing line
cv2.line(line_image, (x51, y51), (x52, y52), (50, 200, 50), 5)
cv2.putText(img, 'line{}'.format(5), (x51, y51), font, 0.8,(0,0,0), 2)
print x51, y51, x52, y52

# drawing line
cv2.line(line_image, (x61, y61), (x62, y62), (50, 50, 200), 5)
cv2.putText(img, 'line{}'.format(6), (x61, y61), font, 0.8,(0,0,0), 2)
print x61, y61, x62, y62


lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)
#print(lines_edges.shape)

cv2.imwrite('line_parking.png', lines_edges)
