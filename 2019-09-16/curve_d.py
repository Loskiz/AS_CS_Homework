#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:47:27 2019

@author: zhangletian
"""

with open("AS_CS_opt2_gradebook.txt") as f1:
    a1=f1.readlines()
for i in range(len(a1)):
    s1=a1[i].split(' ')
    found=False
    for j in s1:
        if j == "Daniel":
            found=True
            break
    if found==True:
        break
s1[4]=str(round(int(s1[3])*1.1))
a1[i]=' '.join(s1)
with open("AS_CS_opt2_gradebook.txt",'w') as f2:
    f2.writelines(a1)