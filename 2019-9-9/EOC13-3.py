#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 23:02:18 2019

@author: zhangletian
"""

#Tally of type list
Tally = [0 for i in range(5)]
#Hobbies of type list
Hobbies = ['Reading','Computer Games','Sport','Programing','TV']
choice=1
while 1:
    choice = int(input('''
                   1 for Reading
                   2 for Computer Games
                   3 for Sport
                   4 for Programing
                   5 for TV
                   0 for STOP
                   '''))
    if choice==0:
        break
    Tally[choice-1]+=1

for i in range(5):
    print(Hobbies[i], end=' ')
    print(Tally[i])
    
a=open('array_data.txt','w')
for j in Tally:
    a.write(str(j)+'\n')
a.close()

b=open('array_data.txt','r')
new_array=[0 for i in range(5)]
i=0
c=b.readline()
d=int(c)
new_array[i]=d
i+=1
while len(c)>0:
    c=b.readline()
    if len(c) !=0:
        d=int(c)
        new_array[i]=d
        i+=1
Tally=new_array
b.close()

