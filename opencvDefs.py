import cv2
import numpy as np
from math import atan

def get_circle_center(frame, lower_hsv, upper_hsv):
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

	circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,2,40,param1=50,param2=10,minRadius=10,maxRadius=50)

	circleCenter = None

	if circles is not None:
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:

			# cv2.circle(img, center,      radius, color[, thickness[, lineType[, shift]]])
			cv2.circle(frame,( i[0], i[1]),  i[2], (255,0,0), 3)
			# draw the center of the circle
			cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

			circleCenter = (i[0], i[1])

	return circleCenter


def draw_action_line(frame, y):
	p1 = (0   , y)
	p2 = (1000, y)
	color = (0,255,255)
	cv2.line(frame, p1, p2, color, 3)



def draw_path_prediction(frame, previousCenter, actualCenter):
	color = (0,165,255)
	m = 1000
	
	if previousCenter != None and actualCenter != None:
		dx = (int(actualCenter[0]) - int(previousCenter[0]))
		dy = (int(previousCenter[1]) - int(actualCenter[1]))
		if abs(dx) < 1:
			ang = 90
		else:
			ang = atan(dy/dx)
		p2x = actualCenter[0] + m*dx
		p2y = actualCenter[1] - m*dy
		p2 = (p2x, p2y)

		cv2.line(frame, actualCenter, p2, color, 3)
		return (actualCenter, p2)


def line_intersection(frame, line1, line2):
	xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)
	# if div == 0:
	#    raise Exception('lines do not intersect')
	if div != 0:
		d = (det(*line1), det(*line2))
		x = int(det(d, xdiff) / div)
		y = int(det(d, ydiff) / div)

		cv2.circle(frame, (x,y), 5, (246, 255, 0), 3)
		return x, y
	return -1, -1
