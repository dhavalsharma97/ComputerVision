#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 3, Question A and B, Using user defined image
"""Finding the edges in an image using canny edge detection and changing the colors of 
edges of different objects. After that, adding salt and pepper noise to the image, 
again applying edge detection algorithm and then removing the noise using median filter."""


#Importing the required libraries
import skimage.io as io
import matplotlib.pyplot as plt
import colorsys
import numpy as np
import cv2

#Converting the image to a numpy array
in_img = io.imread("chrome.jpg")
height = in_img.shape[0]
width = in_img.shape[1]

#Question A begins!
#Detecting the edges using canny edge detection
canny_img_1 = cv2.Canny(image = in_img, threshold1 = 50, threshold2 = 200)

#Adding colors to the image
edge_img_1 = np.zeros(shape = (height, width, 3), dtype = np.uint8)
edges = []

for i in range(height):
    for j in range(width):
        if canny_img_1[i][j] != 0:
            edge_img_1[i][j] = in_img[i][j]
            edges.append(edge_img_1[i][j])

#Finding the mean and standard deviation of all the rgb channels in the edges            
edges = np.array(edges)
mean = np.mean(edges, axis = 0)
std_dev = np.std(edges, axis = 0)

#Changing the color of the found edges to the respective colors in the question
for i in range(height):
    for j in range(width):
        if canny_img_1[i][j] != 0:
            if edge_img_1[i][j][0] > (mean[0] - std_dev[0]) and edge_img_1[i][j][1] < mean[1] and edge_img_1[i][j][2] < mean[2]:
                edge_img_1[i][j][0] = 0
                edge_img_1[i][j][1] = 255
                edge_img_1[i][j][2] = 0
            elif edge_img_1[i][j][1] > (mean[1] - std_dev[1]) and edge_img_1[i][j][0] < mean[0] and edge_img_1[i][j][2] < mean[2]:
                edge_img_1[i][j][0] = 0
                edge_img_1[i][j][1] = 0
                edge_img_1[i][j][2] = 255
            elif edge_img_1[i][j][2] > (mean[2] - std_dev[2]) and edge_img_1[i][j][0] < mean[0] and edge_img_1[i][j][1] < mean[1]:
                edge_img_1[i][j][0] = 255
                edge_img_1[i][j][1] = 0
                edge_img_1[i][j][2] = 0
            elif edge_img_1[i][j][0] > (mean[0] - std_dev[0]) and edge_img_1[i][j][1] > (mean[1] - std_dev[1]) and edge_img_1[i][j][2] < mean[2]:
                edge_img_1[i][j][0] = 0
                edge_img_1[i][j][1] = 255
                edge_img_1[i][j][2] = 255
            elif edge_img_1[i][j][0] < mean[0] and edge_img_1[i][j][1] > (mean[1] - std_dev[1]) and edge_img_1[i][j][2] > (mean[2] - std_dev[2]):
                edge_img_1[i][j][0] = 255
                edge_img_1[i][j][1] = 0
                edge_img_1[i][j][2] = 255
            elif edge_img_1[i][j][0] > (mean[0] - std_dev[0]) and edge_img_1[i][j][1] < mean[1] and edge_img_1[i][j][2] > (mean[2] - std_dev[2]):
                edge_img_1[i][j][0] = 255
                edge_img_1[i][j][1] = 255
                edge_img_1[i][j][2] = 0
            else:
                edge_img_1[i][j][0] = 255
                edge_img_1[i][j][1] = 255
                edge_img_1[i][j][2] = 255
#Question A ends!
                

#Question B begins!
#Adding salt and pepper noise in the image
def salt_pepper(no_of_sp):
    for iteration in range(no_of_sp):
        x_coord = np.random.randint(0, height)
        y_coord = np.random.randint(0, width)
        s_p_img[x_coord][y_coord] = np.random.choice([0, 255])
        
s_p_img = np.copy(in_img)
no_of_sp = int(0.2 * height * width)
salt_pepper(no_of_sp)

#Detecting the edges using canny edge detection
edge_img_2 = cv2.Canny(image = s_p_img, threshold1 = 50, threshold2 = 200)

#Initializing the output image and applying median filter to the image
filt_img = np.zeros(shape = (height, width, 3), dtype = np.uint8)

def med_filt(h, w):
    win_elem = []
    
    for i in range(5):
        for j in range(5):
            win_elem.append(s_p_img[h - 1 + i][w - 1 + j])
    
    win_elem.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb))
    filt_img[h][w] = win_elem[12]

#Loop for traversing through the input image          
for i in range(3, height - 3):
    for j in range(3, width - 3):
        med_filt(i, j)
#Question B ends!
        

#Printing the output image
fig, ax = plt.subplots(nrows = 2, ncols = 2)
ax[0][0].imshow(in_img)
ax[0][1].imshow(edge_img_1)
ax[1][0].imshow(s_p_img)
ax[1][1].imshow(edge_img_2, cmap = 'gray')
plt.show()