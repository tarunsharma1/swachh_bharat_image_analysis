import os
import sys

l=os.listdir('/home/tarun/Downloads/garbage_645/GARBAGE/data/Annotations')
for f in l:
	#f1 = open('/home/tarun/Downloads/garbage_645/GARBAGE/data/Annotations/' + f,'r')
	f1 = open('/home/tarun/fast-rcnn/mine/Annotations/' + f,'r')
	
	lines=f1.readlines()
	new_line1 = lines[-2][:26] + 'Garbage' + lines[-2][35:]
	new_line2 = lines[-1][:27] + 'Garbage' + lines[-1][36:]
	old_lines = lines[:-2]
	final = ''
	for i in old_lines:
		final = final + i
	final = final + new_line1 + new_line2
	
	# new_line1 = lines[0][:24] + 'tarunzeeshan' + lines[0][29:]
	# old_lines = lines[1:]
	# final = ''
	# final = final + new_line1
	# for i in old_lines:
	# 	final = final + i
	
	f2 = open('/home/tarun/fast-rcnn/mine/Annotations/' + f,'w')
	f2.write(final)
	f2.close()	

	f1.close()