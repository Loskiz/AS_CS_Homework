#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n=1
def han(n,fr='a',buffer='b',to='c'):
    if n == 1:
        print(fr+'->'+to)
    else:
        han(n-1,'a','c','b')
        han(1,'a','b','c')
        han(n-1,'b','a','c')
        
