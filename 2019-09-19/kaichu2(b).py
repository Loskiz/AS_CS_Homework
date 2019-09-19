#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:45:26 2019

@author: zhangletian
"""

#a1 of type array
#k of type int

with open('qb.txt') as f1:
    a1=f1.readlines()
bad_student=input('Who do you want to remove: ')
for i in range(len(a1)):
    if a1[i][0:len(bad_student)]==bad_student:
        a1.pop(i)
        break
k=0
with open('qb2.txt','w') as f2:

    for m in range(len(a1)):
        k+=1
        f2.write((4-len(str(k)))*'0'+str(k)+' '+a1[m])