#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:50:18 2019

@author: zhangletian
"""
'''
with open('qbdata.txt') as a:
    for i in a:
        b=i.split(' ')
        if b[-1]>=60:
            print(b[0],b[1],b[-1])
'''        
def my_read(file):
    with open(file) as b:
        for i in b:
            temp=''
            spacecount=0
            for j in i:
                if j!=' ':
                    temp+=j
                elif j==' ':
                    if spacecount==1:
                        temp+=' '
                    spacecount+=1
                if spacecount==2:
                    break
            name=temp
            score=''
            for k in i[-5:]:
                if k != ' ':
                    score+=k
            if float(score)>=60:
                print(name,score)

my_read('qbdata.txt')