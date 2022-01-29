from ctypes import sizeof
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy
image_rgb = img.imread('/Users/yifanliang/Documents/python/Assignment 0/WechatIMG23.jpeg')
image_rgb = image_rgb/255.0
image_grey=0.2989*image_rgb[:,:,0]+0.5870*image_rgb[:,:,1]+0.1140*image_rgb[:,:,2]

plt.imshow(image_grey)
plt.show()
file_output = plt.imsave('outfile.jpeg',image_grey)