import cv2
import os
import glob
import pickle
import sys

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)

l = os.listdir('/home/tarun/Downloads/garbage_1496/GARBAGE/data/Annotations')

annotations = []
for f in l:
	annotations.append(f)




def click_and_crop(event,x,y,flags,params):
	global startx,starty,endx,endy
	global w,h
	global pic
	if event == cv2.EVENT_LBUTTONDOWN:
		#store starting coordinates
		startx = x
		starty = y
	elif event == cv2.EVENT_LBUTTONUP:
		endx = x
		endy = y
		w=	endx - startx
		h= 	endy - starty	
		#print startx, starty,w,h
		cv2.rectangle(pic, (startx, starty),(endx,endy), (0, 255, 0), 2)
		#cv2.imshow('window',pic)
		



path ='/home/tarun/Downloads/garbage_1496/GARBAGE/data/Images/*.jpg'   
files=glob.glob(path)
pic = 0
oldpic = 0
flag = 0 
startx=0
starty=0 
endx = 0
endy=0
w=h=0
final_dict = {}
counter = 0
for file2 in files:
	flag=0
	file2_on_server = file2[0:6] + 'tarunzeeshan' + file2[11:]
	image_name = file2[:-4].split('/')[-1]
	if image_name+'.txt' in annotations:
		print 'image already annotated..skipping'
		continue

	
	pic = cv2.imread(file2)
	#pic = cv2.resize(pic,(1800,1800),interpolation=cv2.INTER_CUBIC)
	oldpic = pic.copy()
	startx=0
	starty=0 
	endx = 0
	endy=0
	w=h=0

	#cv2.namedWindow('window',cv2.WINDOW_NORMAL)
	cv2.namedWindow('window')
	cv2.setMouseCallback('window', click_and_crop)
	while True:
		cv2.imshow('window',pic)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("s"):
			#write values to file
			print startx, starty,w,h
			final_dict[file2] = [startx, starty,w,h]
			counter = counter + 1
			print counter
			f_write = open('/home/tarun/Downloads/garbage_1496/GARBAGE/data/Annotations/'+image_name+'.txt','w')
			f_write.write('Image filename : '+ '\"'+file2_on_server + '\"' + '\n')
			f_write.write('Image size (X x Y x C) : ' + str(pic.shape[0])+' x '+ str(pic.shape[1])+' x ' + str(pic.shape[2])+'\n')
			f_write.write('Objects with ground truth : 1 { \"Garbage\" }' + '\n')
			f_write.write('Original label for object 1 \"Garbage\" : \"Garbage\" \n')
			f_write.write('Center point on object 1 \"Garbage\" (X, Y) : (' + str(startx + w/2)+',' +str(starty + h/2)+')'+'\n')
			f_write.write('Bounding box for object 1 \"Garbage\" (Xmin, Ymin) - (Xmax, Ymax) : (' + str(startx) +',' + str(starty)+') - ('+ str(startx+w) +','+ str(starty+h)+')'+'\n')
			f_write.close()	
			#cv2.imwrite('./testing.jpg',pic)
			break
		elif key== ord("r"):
			#remove rectangle
			pic = oldpic.copy()
			print 'cleared'
		elif key==ord("n"):
			break					

#pickle.dump(final_dict,open("./bounding_box_1496.npy","wb"))						