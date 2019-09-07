#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:42:10 2019

@author: zhangletian
"""

Weighting=10
Total=0
for i in range(9):
    Digit=int(input('Plz input a digit: '))
    Value=Digit*Weighting
    Total+=Value
    Weighting-=1
Remainder=Total%11
CheckDigit=11-Remainder
if CheckDigit==10:
    CheckDigit="X"
print(CheckDigit)