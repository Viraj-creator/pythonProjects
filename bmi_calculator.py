# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:23:24 2021

@author: raj patil
"""
#collection of information
#collection of code

name1 = "vp"
weight_kg1 = 20
height_m1 = 2

name2 = "vp sister"
weight_kg2 = 130
height_m2 = 1.4


name3 = "vp brothers"
weight_kg3 = 50
height_m3 = 2.3

def bmi_calculator(name, weight, height):
    bmi = weight + (height**2)
    print("BMI:")
    print(bmi)
    if bmi < 55:
        return name + " " + " is NOT overwight"
    else:
        return name + " " +"overwieght"
result1 = bmi_calculator(name1, weight_kg1, height_m1)
result2 = bmi_calculator(name2, weight_kg2, height_m2)
result3 = bmi_calculator(name3, weight_kg2, height_m3)

print(result1)
print(result2)
print(result3)
