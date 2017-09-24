import caffe
import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image
import sys
import cv2
import scipy
from scipy import spatial
import pickle
import copy

caffe.set_mode_cpu()
net = caffe.Net('places205CNN_deploy_upgraded.prototxt','places205CNN_iter_300000_upgraded.caffemodel', caffe.TEST)
# net.blobs['data'].data[...] = img
# net.forward()

# print net.blobs['fc7']

before = []
after = []

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', np.load('/home/tarun/caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1))
transformer.set_transpose('data', (2,0,1))
transformer.set_channel_swap('data', (2,1,0))
transformer.set_raw_scale('data', 255.0)


def my_read(img):
	img1 = cv2.imread('./before_after/'+img+'.jpg',0)
	img1 = cv2.resize(img1,(227,227),interpolation = cv2.INTER_AREA)
	img2 = np.zeros((227,227,3))
	img2[:,:,0] = img1
	img2[:,:,1] = img1
	img2[:,:,2] = img1
	
	#img1 = img1[np.newaxis,:, :,:]
	img1 = img2[np.newaxis, :,:,:]
	img1=np.transpose(img1,(0,3,1,2))
	return img1




for i in range(1,29):
	if i==4:
		before.append([0])
		continue
	transformed_image = my_read('before'+str(i))

	v1 = net.blobs['fc7'].data[0]
	o1 = net.forward(data=np.asarray(transformed_image))
	before.append(copy.deepcopy(v1))


for i in range(1,29):
	if i==4:
		after.append([0])
		continue

	transformed_image = my_read('after'+str(i))

	v1 = net.blobs['fc7'].data[0]
	o1 = net.forward(data=np.asarray(transformed_image))
	after.append(copy.deepcopy(v1))



for z,k in enumerate(after):
	if len(k)==1:
		continue
	l = []
	for x,i in enumerate(before):
		if len(i)==1:
			continue
		print  'a'+str(z+1)+', b' + str(x+1), spatial.distance.cosine(k,i)
		l.append(spatial.distance.cosine(k,i))
	print int(l.index(min(l)))	
sys.exit(0)



####### candidate after images ####


im2 = caffe.io.load_image('./images/after4.jpg')
#net.blobs['data'].data[...] = transformer.preprocess('data', im2)

transformed_image2 = transformer.preprocess('data', im2)
transformed_image2 = transformed_image2[np.newaxis,:, :,:]
v2 = net.blobs['fc7'].data[0]

o2 = net.forward(data=np.asarray(transformed_image2))

#o2= net.forward()

l.append(copy.deepcopy(v2))

###########################################
im3 = caffe.io.load_image('./images/after1.jpg')
#net.blobs['data'].data[...] = transformer.preprocess('data', im2)

transformed_image3 = transformer.preprocess('data', im3)
transformed_image3 = transformed_image3[np.newaxis,:, :,:]
v3 = net.blobs['fc7'].data[0]

o3 = net.forward(data=np.asarray(transformed_image3))

#o2= net.forward()

l.append(copy.deepcopy(v3))

###########################################
im4 = caffe.io.load_image('/home/tarun/Downloads/before4.jpg')
#net.blobs['data'].data[...] = transformer.preprocess('data', im2)

transformed_image4 = transformer.preprocess('data', im4)
transformed_image4 = transformed_image4[np.newaxis,:, :,:]
v4 = net.blobs['fc7'].data[0]

o4 = net.forward(data=np.asarray(transformed_image4))

#o2= net.forward()

l.append(copy.deepcopy(v4))


##
print '#########-----------###############'
print 'b1','a4',spatial.distance.cosine(l[0],l[1])
print 'b1','a1',spatial.distance.cosine(l[0],l[2])
print 'a4','a1',spatial.distance.cosine(l[1],l[2])
print 'a4','b4',spatial.distance.cosine(l[1],l[3])
print 'b4','b1',spatial.distance.cosine(l[3],l[0])
print 'a4','a4',spatial.distance.cosine(l[1],l[1])
