#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:23:30 2019

@author: zhangletian
"""

PositiveNumCount=0
NegativeNumCount=0

while 1:
    Num=int(input("Plz input a number: "))
    if Num>0:
        PositiveNumCount+=1
    elif Num<0:
        NegativeNumCount+=1
    elif Num==0:
        break
print(PositiveNumCount,NegativeNumCount)