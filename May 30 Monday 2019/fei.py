# -*- coding: utf-8 -*-
def fei(n):
    l=[1,1]
    for i in range(0,n-2):
        l.append(l[i-2]+l[i-1])
    return l
print(fei(4))