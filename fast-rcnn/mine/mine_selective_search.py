import cv2
import selectivesearch
import sys
import os
import numpy as np
import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab as P
import pickle


#l = os.listdir('/home/tarun/Downloads/INRIA/Train/pos')
l = os.listdir('/home/tarun/ccbd/3k_filtered_final_year_project_second_filtered')

images = []
for f in l:
	if(f[-3:]=='png' or f[-3:]=='jpg' or f[-4:]=='jpeg'):
		images.append(f)


print 'number of images found are ',len(images)

# f = open('/home/tarun/Downloads/inria_25/INRIA/data/ImageSets/train.txt','r')
# l = f.readlines()
# select_images = []
# for name in l:
# 	# remove location and \n
# 	select_images.append(name[:-2]+'.png')

# print len(select_images)
select_images = images

### histogram to see resolution distributions
# sizes = {}
# for img in images:
# 	imgFile = cv2.imread('C:\Users\I337792\Downloads\ccbd_filtered_3k\\files_for_project\\'+img)
# 	h = imgFile.shape[0]
# 	w = imgFile.shape[1]
# 	if (h,w) in sizes.keys():
# 		sizes[(h,w)] += 1
# 	else:
# 		sizes[(h,w)] = 1


# bins = list(sizes.keys())
# bins2 = []

# for i in range(0,len(bins)):
# 	bins2.append((int(bins[i][0]),int(bins[i][1])))

# x= []
# for i in bins:
# 	x.append(sizes[i])


# l = []
# for i in range(0,len(bins)):
# 	l.append((bins2[i],x[i]))

# fig, ax = plt.subplots()
# ax.bar(range(len(l)), [t[1] for t in l]  , align="center")
# ax.set_xticks(range(len(l)))
# ax.set_xticklabels([t[0] for t in l], rotation='vertical')

# plt.show()

#already_done = pickle.load(open('region_dict_25.p','rb'))
already_done = {}
region_dict = {}

for z,img in enumerate(images):
	if img not in select_images:
		continue	
	print z,img
	candidates = []
	if img in already_done.keys():
		region_dict[img] = already_done[img]
		continue
	#imgFile = cv2.imread('/home/tarun/Downloads/INRIA/Train/pos/'+img)
	imgFile = cv2.imread('/home/tarun/ccbd/3k_filtered_final_year_project_second_filtered/'+img)
	
	#cv2.imshow('windows', imgFile)
	#cv2.waitKey(0)
	imgFile = np.array(imgFile, dtype=np.uint8)
	img_lbl, regions = selectivesearch.selective_search(imgFile, scale=500, sigma=0.9, min_size=10)
	#print regions[0:10]
	H,W = imgFile.shape[0], imgFile.shape[1]
	for r in regions:
		#if r['size'] < 500:
		#	continue
		if r['rect'] in candidates:
			continue
		x, y, w, h = r['rect']
		if w<W/8.0 or h<H/8.0:
			continue	
		candidates.append(r['rect'])
	print len(candidates)
	region_dict[img] = candidates
	#print candidates[0]
	#for can in candidates:
	#	cv2.rectangle(imgFile,(can[0],can[1]),(can[0]+can[2],can[1]+can[3]),(0,255,0),1)
	#cv2.imshow('window_new',imgFile)
	#cv2.waitKey(0)

	# save every 50 images
	if z%50==0:
		pickle.dump( region_dict, open( "region_dict_3k_645_"+z+".p", "wb" ) )	


pickle.dump( region_dict, open( "region_dict_3k_645.p", "wb" ) )	
