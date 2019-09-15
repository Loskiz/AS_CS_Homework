#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:59:20 2019

@author: zhangletian
"""

def get_text(file):
    with open(file,'r') as a:
        contents = a.read()
        my_substitutions = contents.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")
        contents = contents.translate(my_substitutions)
    return contents

file='hamlet.txt'
text=get_text(file)
words=text.split()
words.sort()
new_word=words[0]
duprwords=[]
duprwords.append(words[0])
values=[]
total=1
worddic={}
for i in words:
    if i == new_word:
        total+=1
    elif i != new_word:
        values.append(total)
        worddic[i]=total
        total=1
        new_word=i
        duprwords.append(new_word)
ddd={}    
        
xxx=sorted(worddic.items(),key = lambda asd:asd[1],reverse = True)

z=open('sortedwordlist.txt','w')
for i in xxx[0:10]:
    z.write(str(i))
    z.write('\n')
z.close()
    

