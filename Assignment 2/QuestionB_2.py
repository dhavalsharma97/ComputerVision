#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 2, Question B_2
#Finding the equalised histogram and equalised image of an input image

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

#Initialising the equalised histogram array and output image array
eq_hist_arr = []
out_img = []

#Calculating normalization factor
norm_fact = 255 / (height * width)

#Forming the equalised histogram array
eq_hist_arr.append(norm_fact * hist_arr[0])
for i in range(1, 256):
    eq_hist_arr.append(eq_hist_arr[i - 1] + norm_fact * hist_arr[i])

#Converting the equalised histogram array to uint8
eq_hist_arr = np.array(eq_hist_arr)
eq_hist_arr = eq_hist_arr.astype('uint8')

#Forming the output image array
for i in range(height):
    out_img.append([])
    for j in range(width):
        out_img[i].append(eq_hist_arr[in_img[i][j]])

#Plotting and saving the equalised histogram array
gray_levels = np.arange(256)
plt.bar(gray_levels, eq_hist_arr, align = 'center', color = 'blue')
plt.xlabel('Gray levels')
plt.ylabel('Number of pixels')
plt.title('Equalised Histogram')
plt.savefig('Histogram_Equalised.png')

#Saving the output image
out_img = np.array(out_img)
io.imsave('Apple_Equalised.png', out_img)