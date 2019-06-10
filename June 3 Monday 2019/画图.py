# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from copy import deepcopy

image = []


def zero(image, width, height):
    image.clear()
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        image.append(row)


# initialize a two dimensional array filled with zero
zero(image, 640, 640)

"""
Notes on this exercise: Do not modify anything except the content between the dashed lines.
To create a black pixel at row i and column j for image, use image[i][j] = 0. Similarly,
to create a while pixel, use image[i][j] = 255.
You won't need the global width and height variable. They can be retrieved by applying len()
on the "image" passed in.
😏 Good luck and have fun! 🧐
"""


def upperLeftTriangle(image):
    # perform a deep copy, so we won't mess up with the image passed into this function
    image = deepcopy(image)
    # -------------- do whatever you want to "image" -----------
    
    k=0
    for i in range(len(image)):
        for j in range(len(image[i])-k):
            image[i][j]=255
        k+=1
    image.reverse()
    for m in range(len(image)):
        image[m].reverse()
    # ----------------------------------------------------------
    return image


def upperRightTriangle(image):
    # perform a deep copy, so we won't mess up with the image passed into this function
    image = deepcopy(image)
    # -------------- do whatever you want to "image" -----------
    k=0
    for i in range(len(image)):
        for j in range(len(image[i])-k):
            image[i][j]=255
        k+=1
    image.reverse()
    # ----------------------------------------------------------
    return image


def slices(image):
    # perform a deep copy, so we won't mess up with the image passed into this function
    image = deepcopy(image)
    # -------------- do whatever you want to "image" -----------
    T=90
    L=len(image[0])
    counter=0

    for i in range(len(image)):
        image[i]=[]
    for j in range(len(image)):
        for k in range(L):
            if (counter//T)%2==0:
            
                image[j].append(0)
                counter+=1
            else:
                image[j].append(255)
                counter+=1
            if counter==L:
                counter=0
        
    # ----------------------------------------------------------
    return image


# create three subfigures
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

# plot images
ax1.imshow(upperLeftTriangle(image), cmap='gray', vmin=0, vmax=255)
ax2.imshow(upperRightTriangle(image), cmap='gray', vmin=0, vmax=255)
ax3.imshow(slices(image), cmap='gray', vmin=0, vmax=255)
plt.show()