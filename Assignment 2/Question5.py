#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 2, Question 5
#Finding the normalized histogram after applying bit-plane slicing

#Importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

#Initialising the image attributes
in_img = []
height = 206
width = 206
x = 0
x_count = 0

#Initializing the image
for i in range(height):
    in_img.append([])
    for j in range(width):
        if(0 <= x and x <= 100) or (200 <= x and x < 256):
            if(x_count == 206):
                x = x + 1
                x_count = 0
            in_img[i].append(x)
            x_count = x_count + 1
        else:
            if(x_count == 103):
                x = x + 1
                x_count = 0
            in_img[i].append(x)
            x_count = x_count + 1

#Making the image a numpy array
in_img = np.array(in_img)

#Bit plane slicing
for i in range(height):
    for j in range(width):
        if (in_img[i][j] & 64) != 0:
            in_img[i][j] = 255
        else:
            in_img[i][j] = 0

#Initializing histogram array
hist_arr = []
for i in range(256):
    hist_arr.append(0)

#Getting the values for histogram array
for i in range(height):
    for j in range(width):
        hist_arr[in_img[i][j]] = hist_arr[in_img[i][j]] + 1

#Normalizing the histogram array        
for i in range(256):
    hist_arr[i] = hist_arr[i] / (206 * 206)
        
#Plotting the histogram      
gray_levels = np.arange(256)
plt.bar(gray_levels, hist_arr, align = 'center', color = 'blue')
plt.ylim(0, 1)
plt.xlabel('Gray levels')
plt.ylabel('Number of pixels')
plt.title('Normalised Histogram')

#Saving the histogram
plt.savefig('Question5')