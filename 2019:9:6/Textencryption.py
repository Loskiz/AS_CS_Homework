#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:45:26 2019

@author: zhangletian
"""
MyLookup=['i','c','c','s','2','c','3']

def EncryptString(PlainText, Lookup):
    OutString = ''
    for n in range(len(PlainText)):
        OldChar=PlainText[n]
        OldCharValue=ord(OldChar)
        NewChar=Lookup[OldCharValue]
        OutString+=NewChar
    return OutString

def NewEncStr(PlainText, StartPos, NumToChange):
    OutText=list(PlainText)
    n=0
    while n != NumToChange:
        NewChar=input("Please input the sub Char: ")
        OutText[StartPos-1]=NewChar
        n+=1
        StartPos+=1
    print('There are {} elements changed'.format(NumToChange))
    return ''.join(OutText)

for i in range(256):
    MyLookup.append('c')
print(EncryptString('zlt', MyLookup))

print(NewEncStr('ccccccccccccc',1,5))