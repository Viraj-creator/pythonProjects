# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:48:32 2021

@author: raj patil
"""
s = input()
for i in range(0,i+4 < s.length()):
    if s.substr(i,5) == 'party':
        s[i+2] = 'w'
        s[i+3] = 'r'
        s[i+4] = 'i'
        
print(s)       