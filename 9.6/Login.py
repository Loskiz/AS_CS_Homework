#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 23:00:33 2019

@author: zhangletian
"""
UserList=["abc","def"]
PasswordList=["123","456"]

MaxIndex=20
MyUserID=input("ID: ")
MyPassword=input("Password: ")
UserIdFound=False
LoginOK=False
for i in range(MaxIndex):
    if UserList[i]==MyUserID:
        UserIdFound=True
        break
if UserIdFound==True:
    if PasswordList[i]==MyPassword:
        LoginOK=True
if LoginOK==True:
    print("Good")
else:
    print("Failed")
