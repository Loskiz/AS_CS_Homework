#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:49:48 2019

@author: zhangletian
"""

def OuncesToGrams():
    for ounces in range(1,31):
        grams = round(ounces*28.35)
        print(ounces,grams)

def CheckUserID(UserID):
    MyUpperLetters=0
    MyDigits=0
    Valid=False
    for i in UserID:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            MyUpperLetters += 1
        elif ord(i) >= ord('0') and ord(i) <= ord('9'):
            MyDigits += 1
    if MyUpperLetters == 3 and MyDigits == 4:
        Valid=True
    return Valid

