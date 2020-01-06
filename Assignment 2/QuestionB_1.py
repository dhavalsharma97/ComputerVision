#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 2, Question B_1
#Finding the histogram of an image

#Importing the required libraries
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np

#Converting the image to a numpy array
in_img = io.imread('Apple.jpeg')
height = in_img.shape[0]
width = in_img.shape[1]

#Initializing the histogram array
hist_arr = []
for i in range(256):
    hist_arr.append(0)

#Getting the values for histogram array
for i in range(height):
    for j in range(width):
        hist_arr[in_img[i][j]] = hist_arr[in_img[i][j]] + 1

#Plotting the histogram       
gray_levels = np.arange(256)
plt.bar(gray_levels, hist_arr, align = 'center', color = 'blue')
plt.xlabel('Gray levels')
plt.ylabel('Number of pixels')
plt.title('Histogram')

#Displaying and saving the histogram
plt.savefig('Histogram.png')