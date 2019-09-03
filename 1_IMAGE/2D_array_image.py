#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:02:08 2019

@author: zhangletian
"""


MAX_VALUE=255

def ligten(image):
    burnt_out=False
    for row in range(len(image)):
        for column in range(len(image[row])):
            image[row][column]*=1.1
            if image[row][column]>=MAX_VALUE:
                burnt_out=True         
    return burnt_out

def flip(image):
    image2=[]
    for i in range(len(image)):
        image2.append(image[i][::-1])
    return image2

def clip(image):
    
    for row in range(len(image)):
        for column in range(len(image)):
            if image[row][column]>MAX_VALUE:
                image[row][column]=MAX_VALUE
    return image

def ligten2(image):
    for row in range(len(image)):
        for column in range(len(image[row])):
            image[row][column]*=1.1                     
    return image 

from PIL import Image
import numpy as np
filename=input("Please input the file name: ")
my_image=Image.open(filename)
my_image=my_image.convert("L")
#my_image.flags.writeable=True
#my_data=my_image.getdata()
#my_data=np.matrix(my_data)
my_data=np.asarray(my_image)
my_data.setflags(write=1)
my_image.show()

my_data1=flip(my_data)
new_image1=Image.fromarray(np.uint8(my_data1))
new_image1.show()

my_data2=ligten2(my_data)
my_data2=clip(my_data2)
new_image2=Image.fromarray(np.uint8(my_data2))
new_image2.show()
