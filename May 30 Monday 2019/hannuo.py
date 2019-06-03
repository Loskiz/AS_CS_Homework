#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n=1
def han(n,fr='a',buffer='b',to='c'):
    if n == 1:
        print(fr+'->'+to)
    else:
        han(n-1,fr,to,buffer)
        han(1,fr,buffer,to)
        han(n-1,buffer,fr,to)
        