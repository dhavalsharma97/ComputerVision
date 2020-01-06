#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 1
#Enlarging the image by copying the pixels

#Importing the necessary libraries
import skimage.io as io
import numpy as np

#Converting the image to a numpy array
img = io.imread('shox.png')

#Getting the height and width of the image
height = img.shape[0]
width = img.shape[1]

#Getting the multiplier for enlarging the image
k = int(input('Enter the value of k:'))

#Initializing the output array
x = np.zeros(shape = (k * height, k * width, 3), dtype = np.uint8)

#Function for applying enlargement of image
def func(h, w, data):
    h = h * k
    w = w * k
    
    #Loop for copying the data
    for i in range(k):
        for j in range(k):
            x[h + i][w + j] = data

#Loop for traversing through the input image        
for i in range(height):
    for j in range(width):
        func(i, j, img[i][j])
 
#Displaying the image in the output       
io.imshow(x)
io.imsave('shox_enlarged2.png', x)