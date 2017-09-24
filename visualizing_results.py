import cv2
import numpy as np
import os

f = open('results2.txt','rb')
lines = f.readlines()
boxes = {}
for line in lines:
	a = line.split(' ')
	img = a[0]
	xmin = int(float(a[2]))
	ymin = int(float(a[3]))
	xmax = int(float(a[4]))
	ymax = int(float(a[5]))
	if img not in boxes.keys():
		boxes[img] = set()
		boxes[img].add((xmin,ymin,xmax,ymax))
	else:
		boxes[img].add((xmin,ymin,xmax,ymax))

c = 0
for img in boxes.keys():
	print img,len(boxes[img])
	image = cv2.imread('/home/tarun/Downloads/garbage_1454/GARBAGE/data/Images/'+img+'.jpg')
	for box in boxes[img]:
		startx = box[0]
		starty = box[1]
		endx = box[2]
		endy = box[3]
		cv2.rectangle(image, (startx, starty),(endx,endy), (0, 255, 0), 2)
	resized_image = cv2.resize(image, (600, 500)) 	
	cv2.imshow('window',resized_image)
	cv2.waitKey(0)
	#cv2.imwrite('/home/tarun/Downloads/MITplacesCNN/fast-rcnn-test-images/with_bb/'+img+'.jpg',resized_image)
	#c += len(boxes[img])

#print c	