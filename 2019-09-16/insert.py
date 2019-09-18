#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:39:03 2019

@author: zhangletian
"""

with open("AS_CS_opt2_gradebook.txt") as f1:
    a1=f1.readlines()
j=0
for i in range(12):
    j+=1
    a1[i]=str(j)+' '+a1[i]
    
with open("AS_CS_opt2_gradebook.txt",'w') as f2:
    f2.writelines(a1)