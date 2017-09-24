import caffe
caffe.set_mode_cpu()
net1 = caffe.Net('./models/CaffeNet/test_original.prototxt','./data/fast_rcnn_models/caffenet_fast_rcnn_iter_40000.caffemodel',caffe.TEST)
net2 = caffe.Net('./models/CaffeNet/test.prototxt',caffe.TEST)

print net1.params.keys()
print net2.params.keys()

#weights
net2.params['conv1'][0].data[...] = net1.params['conv1'][0].data[...] 
net2.params['conv2'][0].data[...] = net1.params['conv2'][0].data[...] 
net2.params['conv3'][0].data[...] = net1.params['conv3'][0].data[...] 
net2.params['conv4'][0].data[...] = net1.params['conv4'][0].data[...] 
net2.params['conv5'][0].data[...] = net1.params['conv5'][0].data[...] 
net2.params['fc6'][0].data[...] = net1.params['fc6'][0].data[...] 
net2.params['fc7'][0].data[...] = net1.params['fc7'][0].data[...] 

#biases
net2.params['conv1'][1].data[...] = net1.params['conv1'][1].data[...] 
net2.params['conv2'][1].data[...] = net1.params['conv2'][1].data[...] 
net2.params['conv3'][1].data[...] = net1.params['conv3'][1].data[...] 
net2.params['conv4'][1].data[...] = net1.params['conv4'][1].data[...] 
net2.params['conv5'][1].data[...] = net1.params['conv5'][1].data[...] 
net2.params['fc6'][1].data[...] = net1.params['fc6'][1].data[...] 
net2.params['fc7'][1].data[...] = net1.params['fc7'][1].data[...] 

net2.save('./mine_caffenet_iter_40000.caffemodel')