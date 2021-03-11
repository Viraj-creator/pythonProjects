# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:13:12 2020

@author: raj patil
"""

import random
def passwordGenerator():
    
    upperchars = ['A', 'B','C', 'D']
    lowerchars = ['a', 'b','c', 'd']
    specialchars = ['!', '#','$']
    numericchars= ['1', '2' , '3', '4', '5']
    
    password= random.choice(upperchars) + random.choice(lowerchars)+random.choice(specialchars) +random.choice(numericchars) 
    password= password + password  
    print(password)
passwordGenerator()

