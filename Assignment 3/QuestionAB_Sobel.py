#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 3, Question A and B, Using user defined edge detection
"""Finding the edges in an image using user defined edge detection and changing the colors 
of edges of different objects. After that, adding salt and pepper noise to the image, 
again applying edge detection algorithm and then removing the noise using median filter."""


#Importing the required libraries
import skimage.io as io
import math
import numpy as np
import matplotlib.pyplot as plt
import colorsys

#Initializing the input image
in_img = io.imread("pepper.jpg")
height = in_img.shape[0]
width = in_img.shape[1]


#Question A begins!
#Defining the convolution function
def convolution(h, w, window, in_img, out_img):
    sum_of_elem = 0
    
    for i in range(3):
        for j in range(3):
            sum_of_elem = sum_of_elem + (np.average(in_img[h - 1 + i][w - 1 + j]) * window[i][j])
            
    out_img[h][w] = sum_of_elem
    
def sobel_edge_detection(in_img):
    grad_x = np.zeros(shape = (height, width), dtype = np.uint8)
    grad_y = np.zeros(shape = (height, width), dtype = np.uint8)
    magnitude = np.zeros(shape = (height, width), dtype = np.uint8)
    edge_img_1 = np.zeros(shape = (height, width, 3), dtype = np.uint8)
    
    #Output image with x gradient            
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            convolution(i, j, [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], in_img, grad_x)
            
    #Thresholding the image            
    for i in range(height):
        for j in range(width):
            if grad_x[i][j] < 64:
                grad_x[i][j] = 255
    
    # Output image with y gradient
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            convolution(i, j, [[-1, -2, -1], [0, 0, 0], [1, 2, 1]], in_img, grad_y)
            
    #Thresholding the image            
    for i in range(height):
        for j in range(width):
            if grad_y[i][j] < 64:
                grad_y[i][j] = 255
                
    #Output image with magnitude
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            magnitude[i][j] = math.sqrt((grad_x[i][j]) ** 2 + (grad_y[i][j]) ** 2)
            
    #Thresholding the image            
    for i in range(height):
        for j in range(width):
            if magnitude[i][j] < 128:
                magnitude[i][j] = 0
    
    #Adding colors to the image
    edges = []
    
    for i in range(height):
        for j in range(width):
            if magnitude[i][j] != 0:
                edge_img_1[i][j] = in_img[i][j]
                edges.append(edge_img_1[i][j])
    
    #Finding the mean and standard deviation of all the rgb channels in the edges            
    edges = np.array(edges)
    mean = np.mean(edges, axis = 0)
    std_dev = np.std(edges, axis = 0)
    
    #Changing the color of the found edges to the respective colors in the question
    for i in range(height):
        for j in range(width):
            if magnitude[i][j] != 0:
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
    return edge_img_1

#Finding edges using sobel_edge_detecton
edge_img_1 = sobel_edge_detection(in_img)
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
edge_img_2 = sobel_edge_detection(s_p_img)

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