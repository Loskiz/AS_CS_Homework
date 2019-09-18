#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:56:49 2019

@author: zhangletian
"""

with open("AS_CS_opt2_gradebook.txt") as f1:
    a1=f1.readlines()
a2=[]
for i in range(len(a1)):
    s1=a1[i].split(' ')
    a2.append(s1)
a2=sorted(a2,key=lambda s:s[5],reverse=True)
a2.pop()
a2=sorted(a2,key=lambda a:int(a[0]))
a3=[]
for j in a2:
    a3.append(' '.join(j))
with open("new-gradebook.txt",'w') as f2:
    f2.writelines(a3)