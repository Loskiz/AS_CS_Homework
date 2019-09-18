#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:51:09 2019

@author: zhangletian
"""

with open("AS_CS_opt2_gradebook.txt") as f1:
    a1=f1.readlines()
a2=[]
for i in a1:
    a2.append(i[0:-1])
a3=[]    
for j in a2:
    s1=j.split(' ')
    temp=round((int(s1[-1])+int(s1[-2])+int(s1[-3]))/3)
    s1.append(str(temp))
    a3.append(' '.join(s1)+'\n')
with open("AS_CS_opt2_gradebook.txt",'w') as f2:
    f2.writelines(a3)