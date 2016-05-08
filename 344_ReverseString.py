# -*- coding: utf-8 -*-
"""
Created on Sun May  8 13:35:05 2016
The solution of No.344 in LeetCode
https://leetcode.com/problems/reverse-string/
@author: Zhang
"""
from datetime import datetime
def genString(length):
    import random
    out=''
    sta=ord('a')
    end=ord('z')
    for i in range(length):
        inx=random.randint(sta,end)
        out+=chr(inx)
    return out
def reverseString(inStr):
    instring=list(inStr)
    length=len(instring)
    out=''
    for i in range(length):
        out+=instring.pop(-1);
    return out
#This method is faster and easier
def rs(s):
    li=list(s)
    li.reverse()
    out=''
    return out.join(li)

if __name__=='__main__':
    s=genString(999999)
    start=datetime.now()
    a=reverseString(s)
    end=datetime.now()
    print(end.microsecond-start.microsecond)
    start=datetime.now()
    b=rs(s)
    end=datetime.now()
    print(end.microsecond-start.microsecond)
