#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:23:25 2019

@author: zhangletian
"""
import matplotlib.pyplot as plt



def Bsearch(alist, item):
    '''
    this function can check whether a item is in a list
    '''
    alist=sorted(alist)
    found=False
    templ=alist
    while found==False and len(templ)>1:
        midpoint=len(templ)//2
        if item == templ[midpoint]:
            found=True
        elif item>templ[midpoint]:
            templ=templ[midpoint:]
        else:
            templ=templ[:midpoint]
    return found


    
#read the file of the book
def file_to_list(file):
    with open(file) as file_object:
        contents = file_object.read()
        my_substitutions = contents.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")
        contents = contents.translate(my_substitutions)
        contents = contents.split()
    return contents

#remove words used many times from the book
def dupremove(bookL):
    bookL.sort()
    most_recent_element = None
    result=[]
    for word in bookL:
        if word != most_recent_element:
            result.append(word)
            most_recent_element = word
    return result
#see what words are not in the vocablist
def check_words(book,wordlist):
    not_in_list_words=[]
    for word in book:
        resultB=Bsearch(wordlist, word)
        if resultB==False:
            not_in_list_words.append(word)
    return not_in_list_words
            
#count the words
def unknown_word_count(book,wordlist):
    bookL=file_to_list(book)
    wordlistL=file_to_list(wordlist)
    content=dupremove(bookL)
    should_known=wordlistL
    unknownwords=check_words(content,should_known)
    return len(unknownwords)

book='alice_in_wonderland.txt'
wordlist='vocab.txt'
total_none_dup_wordcount=len(dupremove(file_to_list(book)))
unknown_wordcount=unknown_word_count(book,wordlist)
known_wordcount=total_none_dup_wordcount-unknown_wordcount

labels=['Known Words','Unknown Words']
sizes=(known_wordcount,unknown_wordcount)
explode=(0,0.05)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()