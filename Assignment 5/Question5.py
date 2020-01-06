# Author : Dhaval Harish Sharma
# Red ID : 824654344
# Assignment 5, Question 5
# JPEG Compression

# Importing the necessary libraries
import numpy as np
import cv2

# Initializing the input 8X8 Image array
a = np.array([[56, 45, 51, 66, 70, 61, 64, 73],
              [63, 59, 56, 90, 109, 85, 69, 72],
              [62, 59, 68, 103, 144, 104, 66, 73],
              [63, 58, 71, 132, 134, 106, 70, 69],
              [65, 61, 68, 114, 116, 82, 68, 70],
              [79, 65, 60, 67, 77, 68, 58, 75],
              [85, 71, 54, 59, 55, 61, 65, 73],
              [87, 79, 69, 58, 65, 66, 78, 94]])

# Shifting pixels
for i in range(8):
    for j in range(8):
        a[i][j] = a[i][j] - 128

# Computing the descrete cosine transform of the input image
dct_a = np.zeros(shape = (8, 8))
cv2.dct(a / 255, dct_a)
dct_a = (dct_a * 255).astype('int32')

# Initializing the Quantization matrix
q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
              [12, 12, 14, 19, 26, 58, 60, 55],
              [14, 13, 16, 24, 40, 57, 69, 56],
              [14, 17, 22, 29, 51, 87, 80, 62],
              [18, 22, 37, 56, 68, 109, 103, 77],
              [24, 35, 55, 64, 81, 104, 113, 92],
              [49, 64, 78, 87, 103, 121, 120, 101],
              [72, 92, 95, 98, 112, 100, 103, 99]])

# Dividing the input array by the Quantization matrix elementwise
divided_a = np.divide(dct_a, q).astype('int32')

# Traversing the image in a zigzag manner
result = np.empty([8*8])
index = -1
bound = 0

for i in range(0, 15):
    if i < 8:
        bound = 0
    else:
        bound = i - 8 + 1
        
    for j in range(bound, i - bound + 1):
        index += 1
        if i % 2 == 1:
            result[index] = divided_a[j][i - j]
        else:
            result[index] = divided_a[i - j][j]

# Finding the EOB
result = result.astype('int32')
temp = 0
for i in range(len(result)):
    if result[i] != 0:
        temp = i + 1

final_result = []
for i in range(temp):
    final_result.append(result[i])
    
print(final_result)