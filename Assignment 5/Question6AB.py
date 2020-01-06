# Author : Dhaval Harish Sharma
# Red ID : 824654344
# Assignment 5, Question 6AB
# Region Growing Function

# Importing the required libraries
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np
import cv2
import math

def regiongrowing(img, seeds, threshold = 2):
    # This function performs "region growing" in an image from specified
    # seedpoints
    
    # J = regiongrowing(I, seeds, threshold) 
     
    # I : input image 
    # J : logical output image of region
    # seeds : the position of the seedpoints
    # threshold : maximum intensity distance (defaults to 2)

    # The region is iteratively grown by comparing all unallocated neighbouring pixels to the region. 
    # The difference between a pixel's intensity value and the region's mean, 
    # is used as a measure of similarity. The pixel with the smallest difference 
    # measured this way is allocated to the respective region. 
    # This process stops when the intensity difference between region mean and
    # new pixel become larger than a certain threshold (t)
    
    # Example:
    
    # I = plt.imread('Regions.jpg')
    # x = 175
    # y = 175
    # J = regiongrowing(I, [x,y], 4) 
    # plt.imshow(J, cmap='gray')
    
    # Author: D. Kroon, University of Twente
    
    # Dimensions of input image
    dims = img.shape
    
    # Initializing the output arrays
    centroid = []
    area_arr = []
    circularity = []
    
    # Output
    reg = np.zeros(shape = (dims[0], dims[1])).astype('uint8')
    
    for seed in seeds:
        # Initializing the centroid, area and circularity elements
        cir_reg = np.zeros(shape = (dims[0], dims[1])).astype('uint8')
        sum_of_xelements = 0
        sum_of_yelements = 0
        total_elements = 0
        
        # The mean of the segmented region
        mean_reg = float(img[seed[1], seed[0]])
        
        # Number of pixels in region
        size = 1
        pix_area = dims[0] * dims[1]
        
        # Free memory to store neighbours of the (segmented) region
        contour = []
        contour_val = []
        
        # Distance of the region newest pixel to the region mean
        dist = 0
        
        # Neighbor locations (footprint)
        orient = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        cur_pix = [seed[0], seed[1]]
        
        # Start region growing until distance between region and posible new pixels become
        # higher than a certain treshold
        while(dist < threshold and size < pix_area):
        # Add new neighbors pixels
            for j in range(4):
                # Calculate the neighbour coordinate
                temp_pix = [cur_pix[0] + orient[j][0], cur_pix[1] + orient[j][1]]
        
                # Check if neighbour is inside or outside the image
                is_in_img = dims[0] > temp_pix[0] > 0 and dims[1] > temp_pix[1] > 0
                
                # Add neighbor if inside and not already part of the segmented area
                if (is_in_img and (reg[temp_pix[1], temp_pix[0]] == 0)):
                    contour.append(temp_pix)
                    contour_val.append(img[temp_pix[1], temp_pix[0]] )
                    reg[temp_pix[1], temp_pix[0]] = 150
                    cir_reg[temp_pix[1], temp_pix[0]] = 150
                    
            # Add pixel with intensity nearest to the mean of the region, to the region
            dist = abs(int(np.mean(contour_val)) - mean_reg)
        
            dist_list = [abs(i - mean_reg) for i in contour_val]
            dist = min(dist_list)
            index = dist_list.index(min(dist_list))
            size += 1
            reg[cur_pix[1], cur_pix[0]] = 255
            cir_reg[cur_pix[1], cur_pix[0]] = 255
            
            total_elements += 1
            sum_of_xelements += cur_pix[0]
            sum_of_yelements += cur_pix[1]
        
            # Calculate the new mean of the region
            mean_reg = (mean_reg * size + float(contour_val[index])) / (size+1)
            
            # Save the x and y coordinates of the pixel (for the neighbour add proccess)
            cur_pix = contour[index]
        
            # Remove the pixel from the neighbour (check) list
            del contour[index]
            del contour_val[index]
        
        # Calculating the centroid array
        centroid.append([(sum_of_xelements / total_elements), (sum_of_yelements / total_elements)])
        
        # Calculating the area array
        area_arr.append(total_elements)
        
        # Calculating the circularity array
        contours, heirarchy = cv2.findContours(cir_reg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        c = max(contours, key = cv2.contourArea)
        perimeter = cv2.arcLength(c, True)
        area = cv2.contourArea(c)
        circularity.append(4*math.pi*(area/(perimeter**2)))
        
    # Return the segmented area as logical matrix
    return reg, centroid, area_arr, circularity

# Converting the image into numpy array
I = plt.imread('Regions.jpg')
I = (rgb2gray(I) * 255).astype(np.uint8)

# Initializing values and calling regiongrowing
seed1 = [119, 182]
seed2 = [176, 176]
seed3 = [220, 180]

J, centroid, area_arr, circularity = regiongrowing(I, [seed1, seed2, seed3], 5)
print(centroid)
print(area_arr)
print(circularity)

# Printing the output image
fig, ax = plt.subplots(nrows = 1, ncols = 2)
ax[0].imshow(I, cmap = 'gray')
ax[1].imshow(J, cmap = 'gray')