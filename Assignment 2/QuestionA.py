#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 2, Question A
#Finding the distance and speed of the car

#Importing the required libraries
import skimage.io as io
from skimage.color import rgb2gray
import numpy as np
from skimage.util import invert
from skimage.feature import blob_doh

#Converting the image to a numpy array
in_img1 = io.imread('Car1.jpg')
in_img2 = io.imread('Car2.jpg')
height = in_img1.shape[0]
width = in_img1.shape[1]

#Converting the image to grayscale
in_img1_gray = (rgb2gray(in_img1) * 255).astype(np.uint8)
in_img2_gray = (rgb2gray(in_img2) * 255).astype(np.uint8)

#Subtracting the input images
dif = np.zeros(shape = (height, width), dtype = np.uint8)
dif = in_img2_gray - in_img1_gray

#Thresholding the image            
for i in range(height):
    for j in range(width):
        if dif[i][j] < 64:
            dif[i][j] = 255

#Initializing the output image
out_img = np.zeros(shape = (height, width), dtype = np.uint8)

#Function for applying ordered filter for removing noise
def func(h, w):
    win = []
    
    for i in range(3):
        for j in range(3):
            win.append(dif[h - 1 + i][w - 1 + j])
    
    win.sort()
    out_img[h][w] = win[6]

#Loop for traversing through the input image          
for i in range(1, height - 1):
    for j in range(1, width - 1):
        func(i, j)

#Inverting the image colors
out_img = invert(out_img)

#Getting the pixel values of cars
blobs = blob_doh(out_img, max_sigma=100, threshold=0.01)
car1_pix = int(blobs[5][1])
car2_pix = int(blobs[8][1])

#Calculating the speed of the car
total_dist_image = 35.06
print("Total distance of the image frame:", total_dist_image, "meters")
pix_trav_car = abs(car2_pix - car1_pix)
print("Total pixels travelled by car:", pix_trav_car, "pixels")
total_dist_car = (pix_trav_car * total_dist_image) / width
print("Total distance travelled by car:", total_dist_car, "meters")
time = 1.93
print("Time between both frames:", time, "seconds")
speed_mps = total_dist_car / time
speed_mph = speed_mps * 2.237
print("Speed:", speed_mps, "meters/second")
print("Speed:", speed_mph, "miles/hour")

#Printing the output image
print("\nOutput Image:")
io.imshow(out_img)