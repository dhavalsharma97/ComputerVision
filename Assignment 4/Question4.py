#Author : Dhaval Harish Sharma
#Red ID : 824654344
#Assignment 4, Question 4
"""Propose the equation of a Gaussian bandpass filter with a bandwidth w and cutoff 
frequency r0"""

#Importing the required libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from skimage.color import rgb2gray

#Converting the image into numpy array
in_img = plt.imread("Finger.png")
in_img = (rgb2gray(in_img) * 255).astype(np.uint8)

#Padding zeros to make the dimensions of image a power of 2
def next_pow(num):
    return math.ceil(math.log(num,2))

nextpow = next_pow(max(in_img.shape[0], in_img.shape[1]))
padded_img = np.zeros(shape = (2**nextpow, 2**nextpow), dtype = np.uint8)
for i in range(in_img.shape[0]):
    for j in range(in_img.shape[1]):
        padded_img[i][j] = in_img[i][j]

#Making the gaussian bandpass filter
x = np.linspace(-padded_img.shape[0] // 2, padded_img.shape[0] // 2 - 1, padded_img.shape[0])
y = np.linspace(-padded_img.shape[1] // 2, padded_img.shape[1] //2 - 1, padded_img.shape[1])
[u, v] = np.meshgrid(x, y)
r_sq = u**2 + v**2
r0_sq = 35**2

#gbpf = 1 - np.exp(-(1/2) * (w / (r_sq - r0_sq))**2)
gbpf = 1 - np.exp(-(1/2) * (600 / (r_sq - r0_sq))**2)

#Applying FFT on the images
padded_img_fft = np.fft.fftshift(np.fft.fft2(padded_img))
padded_img_filtered = padded_img_fft * gbpf
padded_img_inverse = np.fft.ifft2(padded_img_filtered)

#Getting the output image from padded image
out_img = np.zeros(shape = (in_img.shape[0], in_img.shape[1]), dtype = padded_img_inverse.dtype)
for i in range(in_img.shape[0]):
    for j in range(in_img.shape[1]):
        out_img[i][j] = padded_img_inverse[i][j]

#Printing the output image
fig, ax = plt.subplots(nrows = 2, ncols = 3)
ax[0][0].imshow(in_img, cmap = 'gray')
ax[0][1].imshow(gbpf, cmap = plt.cm.gray)
ax[0][2].imshow((np.log(1 + np.abs(padded_img_fft))).astype(int), cmap = plt.cm.gray)
ax[1][0].imshow((np.log(1 + np.abs(padded_img_filtered))).astype(int), cmap = plt.cm.gray)
ax[1][1].imshow(np.abs(padded_img_inverse).astype(int), cmap = plt.cm.gray)
ax[1][2].imshow(np.abs(out_img).astype(int), cmap = plt.cm.gray)