#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:38:47 2019

@author: zhangletian
"""

RogueValue=-1
Total=0
Count=0
Number=int(input("Please input a number: "))
while Number!=RogueValue:
    Count+=1
    Total+=Number
    Number=int(input("Please input a number: "))
if Count>0:
    Average=Total/Count
    print(Average)