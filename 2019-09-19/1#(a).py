#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:34:19 2019

@author: zhangletian
"""

#a1, a2 of type array
#s1 of type string


char=input('Please input a char: ')
with open('qb.txt') as f1:
    a1=f1.readlines()
a2=[]
for i in a1:
    s1=''
    for j in i:
        if j!=' ':
            s1+=j
        else: 
            s1+=char
    a2.append(s1)
with open('new_qb.txt','w') as f2:
    f2.writelines(a2)       