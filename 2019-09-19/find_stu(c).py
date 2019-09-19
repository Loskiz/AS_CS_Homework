#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:59:02 2019

@author: zhangletian
"""
#please run kaichu2.py first

#a1 of type array
#found of type bool

code=input('Please input the code for the student: ')
with open('qb2.txt') as f1:
    a1=f1.readlines()
found=False
for i in a1:
    if i[0:4]==code:
        print(i)
        found=True
if found==False:
    print('Student not found')
    