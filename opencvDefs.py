import cv2
import numpy as np

def getCircleCenter(frame, lower_hsv, upper_hsv):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,2,40,param1=50,param2=10,minRadius=10,maxRadius=50)

    circleCenter = (0,0)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:

            # cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
            cv2.circle(frame,(  i[0],  i[1]),  i[2], (255,0,0), 3)
            # draw the center of the circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

            circleCenter = (i[0], i[1])

    return circleCenter