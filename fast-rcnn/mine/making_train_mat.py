import pickle
import numpy as np
import sys
import os
import scipy.io

# scipy.io.savemat('/tmp/out.mat', mdict={'exon': obj_arr})
region_dict = pickle.load(open('./region_dict_.p','rb'))

f = open('/home/tarun/Downloads/inria_25/INRIA/data/ImageSets/train.txt','rb')
l = f.readlines()

print len(l)

c= []
for img in l:
	img = img[:-2]+'.png'
	#print img
	num_boxes = len(region_dict[img])
	b = []
	for box in region_dict[img]:
		box = list(box)
		box[2] = box[2] + box[0]
		box[3] = box[3] + box[1]
		b.append(np.array(box))
	b = np.array(b)
	#print b.shape
	c.append(b)
c= np.array(c)
scipy.io.savemat('/home/tarun/Downloads/inria_100/INRIA/train.mat', mdict={'all_boxes': c})
#print c.shape	