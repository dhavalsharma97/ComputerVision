#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 4, Question 2(B)
"""Now apply a low pass spatial domain filter (such as an averaging filter) to the above 
three images and compare the results with those obtained in (a)."""

#Importing the required libraries
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np

#Taking the image from user
print("The available images: 1) Blonde1 2) Blonde2 3) Zebra")
temp = input("Please enter the image to filter:")
if temp == "1":
    in_img = plt.imread("Blonde1.jpg")
elif temp == "2":
    in_img = plt.imread("Blonde2.jpg")
elif temp == "3":
    in_img = plt.imread("Zebra.jpg")
    in_img = (rgb2gray(in_img) * 255).astype(np.uint8)
else:
    print("Please enter correct name!")

#Getting the height and width of the image
height = in_img.shape[0]
width = in_img.shape[1]

#Initializing the output image
out_img = np.zeros(shape = (height, width), dtype = np.uint8)

#Function for applying the averaging filter on the image
def averaging(h, w):
    
    window = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    sum1 = 0
    
    for i in range(3):
        for j in range(3):
            sum1 = sum1 + (in_img[h - 1 + i][w - 1 + j] * window[i][j])
    
    out_img[h][w] = sum1 // 9
            
#Traversing the image and applying the averaging filter
for i in range(1, height - 1):
    for j in range(1, width - 1):
        averaging(i, j)

#Printing the output image
plt.imshow(out_img, cmap = 'gray')