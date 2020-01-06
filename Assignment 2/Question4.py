#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 2, Question 4
#Finding the normalized histogram after contrast mapping

#Importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

#Initialising the image attributes
height = 256
width = 256
in_img = []

#Initializing the input image
for i in range(height):
    in_img.append([])
    gray_value = 0
    for j in range(width):
        in_img[i].append(gray_value)
        gray_value = gray_value + 1
in_img = np.array(in_img)

#Initialising the output image
out_img = []

#Applying mapping function on the input image
for i in range(height):
    out_img.append([])
    for j in range(width):
        if 0 <= in_img[i][j] and in_img[i][j] <= 119:
            out_img[i].append(0.4 * in_img[i][j])
        else:
            out_img[i].append(in_img[i][j])
            
#Function for applying multiple passes of mapping           
def map(in_arr):
    for i in range(height):
        for j in range(width):
            if 0 <= in_arr[i][j] and in_arr[i][j] <= 119:
                in_arr[i][j] = 0.4 * in_arr[i][j]
            else:
                pass
    return in_arr

#Applying passes of mapping on output image
for i in range(100):
    out_img = map(out_img)
    
#Removing the float values from output image
out_img = np.array(out_img)
out_img = out_img.astype('uint8')

#Initialising the histogram array
eq_hist_arr = []
for i in range(256):
    eq_hist_arr.append(0)

#Getting the values for histogram array
for i in range(height):
    for j in range(width):
        eq_hist_arr[out_img[i][j]] = eq_hist_arr[out_img[i][j]] + 1
        
#Normalising the histogram
for i in range(256):
    eq_hist_arr[i] = eq_hist_arr[i] / (height * width)

#Plotting the histogram      
gray_levels = np.arange(256)
plt.bar(gray_levels, eq_hist_arr, align = 'center', color = 'blue')
plt.ylim(0, 1)
plt.xlabel('Gray levels')
plt.ylabel('Number of pixels')
plt.title('Normalised Histogram')

#Saving the histogram
plt.savefig('Question4')