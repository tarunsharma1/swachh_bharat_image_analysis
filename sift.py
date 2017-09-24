import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
gray1 = cv2.imread('./images/before1.jpg',0)
#sift = cv2.xfeatures2d.SIFT_create()
orb = cv2.ORB()
kp1 = orb.detect(gray1,None)
kp1,des1 =orb.compute(gray1,kp1)

print len(des1[1]),des1[0]
sys.exit(0)
img1=cv2.drawKeypoints(gray1,kp1,color=(0,255,0),flags=0)
cv2.imshow('before',img1)

# img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
gray2 = cv2.imread('./images/after1.jpg',0)
#sift = cv2.xfeatures2d.SIFT_create()
kp2 = orb.detect(gray2,None)
kp2,des2 =orb.compute(gray2,kp2)

img2=cv2.drawKeypoints(gray2,kp2,color=(0,255,0),flags=0)
cv2.imshow('after',img2)
cv2.waitKey(0)
