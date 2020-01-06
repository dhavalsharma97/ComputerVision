#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 1
#Enlarging the image using bilinear interpolation

#Importing the necessary libraries
import skimage.io as io
import numpy as np

#Converting the image to a numpy array
in_img = io.imread('shox.png')

#Getting the height and width of the image
height = in_img.shape[0]
width = in_img.shape[1]

#Getting the multiplier for enlarging the image
k = int(input('Enter the value of k:'))

#Initializing the output array
out_img = np.zeros(shape = (height * k, width * k, 3), dtype = np.uint8)

#Function for applying bilinear interpolation
def func(h, w, data):
    h_ptr = h * k
    w_ptr = w * k
    out_img[h_ptr][w_ptr] = data
    
    #Loop for applying bilinear interpolation on the first row
    for i in range(1, k):
        out_img[h_ptr][w_ptr + i] = (((w_ptr + k) - (w_ptr + i)) / ((w_ptr + k) - (w_ptr - k))) * in_img[h][w] + (((w_ptr + i) - (w_ptr - k)) / ((w_ptr + k) - (w_ptr - k))) * in_img[h][w + 1]
    
    #Loop for applying bilinear interpolation on the last row    
    for i in range(k):
        out_img[h_ptr + k - 1][w_ptr + i] = (((w_ptr + k) - (w_ptr + i)) / ((w_ptr + k) - (w_ptr - k))) * in_img[h+1][w] + (((w_ptr + i) - (w_ptr - k)) / ((w_ptr + k) - (w_ptr - k))) * in_img[h+1][w + 1]
    
    #Loop for applying bilinear interpolation on the intermediate rows
    for i in range(1, k - 1):
        for j in range(k):
            out_img[h_ptr + i][w_ptr + j] = (((h_ptr + k) - (h_ptr + i)) / ((h_ptr + k) - (h_ptr - k))) * out_img[h_ptr][w_ptr + j] + (((h_ptr + i) - (h_ptr - k)) / ((h_ptr + k) - (h_ptr - k))) * out_img[h_ptr + k - 1][w_ptr + j]

#Loop for traversing through the input image
for h in range(height - 1):
    for w in range(width - 1):
        func(h, w, in_img[h][w])

#Displaying the image in the output        
io.imshow(out_img)
io.imsave('shox_enlarged1.png', out_img)