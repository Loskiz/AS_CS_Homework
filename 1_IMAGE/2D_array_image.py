#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:02:08 2019

@author: zhangletian
"""
from PIL import Image

MAX_VALUE=255

def ligten(image):
    burnt_out=False
    for row in range(len(image)):
        for column in range(len(image[row])):
            image[row][column]*=1.1
            if image[row][column]>MAX_VALUE:
                burnt_out=True 
                break
        if burnt_out==True:
            break
    return burnt_out

def flip(image):
    for row in range(len(image)):
        image[row].reverse()
    return(image)

def clip(image):
    
    for row in range(len(image)):
        for column in range(len(image)):
            if image[row][column]>MAX_VALUE:
                image[row][column]=MAX_VALUE
    return(image)
   
image=[[245,2,3],[2,3,4]]
a=ligten(image)
b=flip(image)
b=clip(image)
print(a)
print(b)

