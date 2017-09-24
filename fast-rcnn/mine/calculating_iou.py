import cv2
import sys

def bb_intersection_over_union(boxA, boxB):
	# determine the (x, y)-coordinates of the intersection rectangle
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])
 
	# compute the area of intersection rectangle
	interArea = (xB - xA + 1) * (yB - yA + 1)
 	
	# compute the area of both the prediction and ground-truth
	# rectangles
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
 
	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(boxAArea + boxBArea - interArea)
 
	# return the intersection over union value
	return iou

mean_iou = []
f= open('./results.txt','r')
lines = f.readlines()
f.close()
count = 0
for line in lines:
	img = line.split(' ')[0]
	pred = []
	for i in line.split(' ')[1:]:
		pred.append(float(i))

	# read ground truth from annotation file
	f = open('/home/tarun/Downloads/garbage_1454/GARBAGE/data/Annotations/'+img+'.txt','r')
	l = f.readlines()
	f.close()
	l = l[-1]
	l = l.split(' : ')[1].split(' - ')
	x1 =  float(l[0].split(',')[0][1:])
	y1 =  float(l[0].split(',')[1][:-1])
	x2 =  float(l[1].split(',')[0][1:])
	y2 =  float(l[1].split(',')[1][:-2])
	gt = [x1,y1,x2,y2]
	iou = bb_intersection_over_union(gt,pred)
	print iou
	if iou < 0:
		iou = -1 * iou
	if iou > 0.1:
		count = count + 1	
	mean_iou.append(iou)

print sum(mean_iou)/len(mean_iou)
print count, len(mean_iou)		