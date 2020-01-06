#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 3, Question 3
#Finding the edges using sobel edge detection

#Importing the required libraries
import skimage.io as io
import numpy as np
import math

#Initializing the input image
in_img = []
for i in range(8):
    in_img.append([])
    for j in range(8 - i):
        in_img[i].append(2)
    for k in range(i):
        in_img[i].append(7)
        
in_img = np.array(in_img).astype(np.uint8)
out_img_1 = np.zeros(shape = (8, 8), dtype = np.uint8)
out_img_2 = np.zeros(shape = (8, 8), dtype = np.uint8)
out_img_3 = np.zeros(shape = (8, 8), dtype = np.uint8)

#Defining the convolution function
def convolution(h, w, kernel, out):
    
    window = kernel
    out_img = out
    sum1 = 0
    
    for i in range(3):
        for j in range(3):
            sum1 = sum1 + (in_img[h - 1 + i][w - 1 + j] * window[i][j])
    
    out_img[h][w] = sum1

#Output image with x gradient            
for i in range(1, 7):
    for j in range(1, 7):
        convolution(i, j, [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], out_img_1)

# Output image with y gradient
for i in range(1, 7):
    for j in range(1, 7):
        convolution(i, j, [[-1, -2, -1], [0, 0, 0], [1, 2, 1]], out_img_2)

#Output image with magnitude
for i in range(1, 7):
    for j in range(1, 7):
        out_img_3[i][j] = math.sqrt((out_img_1[i][j]) ** 2 + (out_img_2[i][j]) ** 2)

#Printing the image    
io.imshow(out_img_3)