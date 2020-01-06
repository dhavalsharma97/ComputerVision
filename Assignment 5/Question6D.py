# Author : Dhaval Harish Sharma
# Red ID : 824654344
# Assignment 5, Question 6D
# Region Growing Function

# Importing the required libraries
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np
import cv2

def regiongrowing(img, threshold = 2):
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
    
    # Getting the red color of the beans from the image
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(img_hsv, (120,110,100), (125,180,200))
    red_beans = cv2.bitwise_and(img, img, mask = mask1)
    
    # Getting the yellow color of the beans from the image
    mask2 = cv2.inRange(img_hsv, (90,150,200), (104,190,255))
    yellow_beans = cv2.bitwise_and(img, img, mask = mask2)
    
    # Getting the circular red and yellow beans from the image
    gray_img = (rgb2gray(red_beans + yellow_beans) * 255).astype(np.uint8)
    circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, 1.4, 10)
    
    # Getting the seeds and the grayscale image
    img = (rgb2gray(img) * 255).astype(np.uint8)
    seeds = circles[0].astype(int)

    # Dimensions of input image
    dims = img.shape
    
    # Output
    reg = np.zeros(shape = (dims[0], dims[1])).astype('uint8')
    
    # Initializing the nearest elements array
    nearest_elements = []
    
    for seed in seeds:
        
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
                    
            # Add pixel with intensity nearest to the mean of the region, to the region
            dist = abs(int(np.mean(contour_val)) - mean_reg)
        
            dist_list = [abs(i - mean_reg) for i in contour_val]
            dist = min(dist_list)
            index = dist_list.index(min(dist_list))
            size += 1
            reg[cur_pix[1], cur_pix[0]] = 255
            
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
            
        # Calculating the distance array
        nearest_elements.append([(sum_of_xelements / total_elements), (sum_of_yelements / total_elements)])
        min_dist = abs(nearest_elements[0] - nearest_elements[1])
        
    # Return the segmented area as logical matrix
    return reg, min_dist

# Converting the image into numpy array
I = plt.imread('Beans.jpg')

# Calling regiongrowing
J, min_dist = regiongrowing(I, 25)

# Printing the minimum distance
print(min_dist)

# Printing the output image
fig, ax = plt.subplots(nrows = 1, ncols = 2)
ax[0].imshow(I, cmap = 'gray')
ax[1].imshow(J, cmap = 'gray')