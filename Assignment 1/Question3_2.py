#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 1
#Reflecting the image about its x-axis

#Importing the necessary libraries
import skimage.io as io
import numpy as np

#Converting the image to a numpy array
in_img = io.imread('shox.png')

#Getting the number of pixels in the image
print("Shape of the image:", in_img.shape)

#Initializing an empty array
out_img = []

#Logic for reflecting the image
for i in range(in_img.shape[0]):
    out_img.append([])
    for j in range(in_img.shape[1]):
        out_img[i].append(in_img[i][in_img.shape[1] - 1 - j])
 
#Converting the list to a numpy array       
out_img = np.array(out_img)

#Displaying the image in the output
io.imshow(out_img)
io.imsave('shox_reflected2.png', out_img)